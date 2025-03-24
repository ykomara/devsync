from django.urls import path, include
from . import views

from .views import UserAPIView
from .views import ProjectAPIView
from .views import  TaskAPIView
from .views import UserAPIView

urlpatterns = [
    path('', views.index, name="index"),
    path('api/users/', UserAPIView.as_view()),
   path('api/projects/', ProjectAPIView.as_view()),
   path('api/tasks/', TaskAPIView.as_view())
]
