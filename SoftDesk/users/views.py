from django.shortcuts import render
from .models import User, Contributor
from rest_framework import viewsets
from .serializers import UserSerializer, ContributorProjectSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get("username")
        if User.objects.filter(username=username).exists():
            # Handle case where username already exists (return an error response or take another action)
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            email=serializer.validated_data.get("email"),
            first_name=serializer.validated_data.get("first_name", ""),
            last_name=serializer.validated_data.get("last_name"),
            username=username,
        )

        user.set_password(serializer.validated_data.get("password"))
        user.save()

        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            
            
            if serializer.is_valid():
                self.perform_update(serializer)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
class ContributorProjectViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorProjectSerializer
    permission_classes = [IsAuthenticated]
