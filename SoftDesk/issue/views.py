from django.shortcuts import render
from rest_framework import viewsets
from issue.serializers import IssueSerializer
from Project.models import Project
from .models import Issue
# Create your views here.
class IssueViewSets(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer