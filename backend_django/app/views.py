from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


# Create your views here.
def index(request):
    return HttpResponse("Bonjour")

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer