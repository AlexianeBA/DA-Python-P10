
from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class CommentViewSets(viewsets.ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]