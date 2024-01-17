
from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.
class CommentViewSets(viewsets.ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class = CommentSerializer