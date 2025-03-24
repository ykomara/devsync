from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Project, Task
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer


def index(request):
    return HttpResponse("Bonjour")


# Create your views here.

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





