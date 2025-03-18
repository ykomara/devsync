from rest_framework import serializers
from .models import User, Project, Task

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model=User
        fields=['id', 'username', 'email', 'is_staff']

class ProjectSerializer(serializers.ModelSerializer):
    class meta:
        model= Project
        fields=['name', 'description', 'owner', 'members']

class TaskSerializer(serializers.ModelSerializer):
    class meta:
        model=Task
        fields=['title', 'description', 'status', 'priority', 'project', 'assignee']

