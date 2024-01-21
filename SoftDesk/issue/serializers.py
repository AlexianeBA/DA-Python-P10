from rest_framework import serializers
from .models import Issue
from Project.models import Project

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Issue
        fields=['title', 'description', 'tag', 'priority', 'status', 'project', 'author', 'assigned', 'created']
      
