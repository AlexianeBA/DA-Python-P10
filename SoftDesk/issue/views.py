from django.shortcuts import render
from rest_framework import viewsets
from issue.serializers import IssueSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOfIssue, IsContributorOFIssue
from rest_framework.pagination import PageNumberPagination
from .models import Issue
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class IssueViewSets(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthorOfIssue, IsContributorOFIssue]
    pagination_class = PageNumberPagination

    def list(self, request):
        query = request.GET.get("query", None)

        if query is not None:
            query_set = Issue.objects.filter(title__icontains=query)
        else:
            query_set = Issue.objects.all()

        return Response(
            self.serializer_class(query_set, many=True).data, status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user = request.user
        data = {
            "title": request.data.get("title", None),
            "description": request.data.get("description", None),
            "tag": request.data.get("tag", None),
            "priority": request.data.get("priority", None),
            "status": request.data.get("status", None),
            "project": request.data.get("project", None),
            "author": request.data.get("author", None),
            "assigned": request.data.get("assigned", None),
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
        return super(IssueViewSets, self).destroy(request, pk, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance, data=request.data, partial=kwargs.pop("partial", False)
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
