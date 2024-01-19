from rest_framework import serializers
from .models import Issue
from Project.models import Project

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Issue
        fields=['title', 'description', 'tag', 'priority', 'status', 'project', 'author', 'assigned', 'created']
        #méthode à mettre dans views + à modifier
        def create(self, serializer):
            author = self.context.get("request", None).user
            assigned = self.context.get("request", None).user
            project = Project.objects.get(pk=self.context.get("view").kwargs["project_pk"])

            issue= Issue.objects.create(title=serializer["title"],
            desc=serializer["desc"],
            tag=serializer["tag"],
            priority=serializer["priority"],
            project=project,
            status=serializer["status"],
            author=author,
            assigned=assigned)
            
            issue.save()
            return issue