from django.urls import path, include
from rest_framework import routers
from. import views
from .views import RegisterView

"""
from .views import UserAPIView, ProjectAPIView, TaskAPIView

urlpatterns = [
    path('', views.index, name="index"),
    path('api/users/', UserAPIView.as_view()),
   path('api/projects/', ProjectAPIView.as_view()),
   path('api/tasks/', TaskAPIView.as_view())
]
"""
router = routers.SimpleRouter()
router.register('users', views.UserViewset, basename='users')
router.register('projects', views.ProjectViewset, basename='projects')
router.register('tasks', views.TaskViewset, basename='tasks')

urlpatterns = [
    path('', views.index, name="index"),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
]







