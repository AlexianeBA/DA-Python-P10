from rest_framework import serializers
from .models import User, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'age','date_of_birth', 'can_be_contacted', 'can_data_be_shared']
        
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'type_project', 'created_at']