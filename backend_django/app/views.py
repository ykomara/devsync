from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Project, Task
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer
from rest_framework.viewsets import ModelViewSet

def index(request):
    return HttpResponse("Bonjour je suis Yaya KOMARA ingénieur logiciel")

class UserViewset(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()

class ProjectViewset(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProjectSerializer
    def get_queryset(self):
        return Project.objects.all()

class TaskViewset(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.all()

"""
class UserAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
       users=User.objects.all()
       serializer=UserSerializer(users, many=True)
       return Response(serializer.data)

class ProjectAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        projects=Project.objects.all()
        serializer=ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class TaskAPIView(APIView):
    def get(self, *args, **kwargs):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks, many=True)
        return Response(serializer.data)

"""
# Create your views here.







