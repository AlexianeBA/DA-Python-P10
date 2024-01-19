from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
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
    
#méthode à implémenter dans chaque views
    def list(self, request):
        query = request.GET.get('query', None)
        
        if query is not None:
            query_set = Project.objects.filter(title__icontains=query)
        else:
            query_set = Project.objects.all()

        return Response(self.serializer_class(query_set, many=True).data, status=status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        user = request.user
        data = {
            "title": request.data.get('title', None),
            "type_project": request.data.get('type_project', None),
            "author": request.data.get('author', None),
        }

        serializer = self.serializer_class(data=data, context={'author': user})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return super(ProjectViewSet, self).destroy(request, pk, *args, **kwargs)
    
    
    def update(self, request, *args, **kwargs):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            
            
            if serializer.is_valid():
                self.perform_update(serializer)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        