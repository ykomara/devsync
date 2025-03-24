from rest_framework.serializers import ModelSerializer
from .models import User, Project, Task

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'full_name', 'email', 'is_staff']

class ProjectSerializer(ModelSerializer):
    class Meta:
        model= Project
        fields=['name', 'description', 'owner', 'members']

class TaskSerializer(ModelSerializer):
    class Meta:
        model=Task
        fields=['title', 'description', 'status', 'priority', 'project', 'assignee']

