from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import User, Project, Task
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer


# Create your views here.
def index(request):
    return HttpResponse("Bonjour")

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]