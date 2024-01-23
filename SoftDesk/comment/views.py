from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOfComment
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOfComment]

    def list(self, request):
        query = request.GET.get("query", None)

        if query is not None:
            query_set = Comment.objects.filter(title__icontains=query)
        else:
            query_set = Comment.objects.all()

        return Response(
            self.serializer_class(query_set, many=True).data, status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user = request.user
        data = {
            "description": request.data.get("description", None),
            "issue": request.data.get("issue", None),
            "author": request.data.get("author", None),
        }

        serializer = self.serializer_class(data=data, context={"author": user})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return super(CommentViewSets, self).destroy(request, pk, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
