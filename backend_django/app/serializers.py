from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Project, Task

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'full_name', 'email', 'is_staff']

class RegisterSerializer(ModelSerializer):
    password= serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'password', 'role']

    def create(self, validated_data):
        password= validated_data.pop('password')
        user= User.objects.create_user(password=password, **validated_data)
        return user


class ProjectSerializer(ModelSerializer):
    class Meta:
        model= Project
        fields=['name', 'description', 'owner', 'members']

class TaskSerializer(ModelSerializer):
    class Meta:
        model=Task
        fields=['title', 'description', 'status', 'priority', 'project', 'assignee']

