from django.shortcuts import render
from .models import User, Contributor
from rest_framework import viewsets
from .serializers import UserSerializer, ContributorProjectSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            age = serializer.validated_data.get("age", instance.age)
            if age is not None and age < 15:
                serializer.validated_data["can_data_be_shared"] = "Non"
            self.perform_update(serializer)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContributorProjectViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorProjectSerializer
    permission_classes = [IsAuthenticated]
