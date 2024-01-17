from django.shortcuts import render
from .models import User, Contributor
from rest_framework import viewsets
from .serializers import UserSerializer, ContributorProjectSerializer

from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class ContributorProjectViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorProjectSerializer
    permission_classes = [IsAuthenticated]
