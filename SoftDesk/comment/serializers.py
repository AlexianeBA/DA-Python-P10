from rest_framework import serializers
from .models import Comment
from issue.serializers import IssueSerializer


class CommentSerializer(serializers.ModelSerializer):
    issue = IssueSerializer()

    class Meta:
        model = Comment
        fields = ["id", "description", "issue", "author"]
