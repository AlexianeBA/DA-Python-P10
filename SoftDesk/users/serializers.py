from rest_framework import serializers
from .models import User, Contributor
from Project.models import Project
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'age','date_of_birth', 'can_be_contacted', 'can_data_be_shared']
        
        
        def create(self, serializer):
            user = User.objects.create(
                email=serializer["email"],
                first_name=serializer["first_name"],
                last_name=serializer["last_name"],
            )

            user.set_password(serializer["password"])
            user.save()
            return user
        
        
class ContributorProjectSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Contributor
        fields = ('id',
                  'user',
                  'project',
                  )

    def validate_user(self, value):
        user = self.context['request'].user
        if user == value:
            raise serializers.ValidationError(
                "L'auteur du projet ne peut pas être contributeur")
        return value

    def perform_create(self, serialize):
        projet = Project.objects.get(pk=self.context.get("view").kwargs["project_pk"])

        contributor = Contributor.objects.create(
            user=serialize["user"],
            project=projet
        )
        contributor.save()
        return contributor