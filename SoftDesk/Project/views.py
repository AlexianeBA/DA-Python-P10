from django.shortcuts import render

from .models import Project
from rest_framework import viewsets
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from users.models import Contributor
# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    
