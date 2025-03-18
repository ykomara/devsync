from django.urls import path, include
from rest_framework import routers

from . import views
from .views import UserViewSet, ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name="index")
]