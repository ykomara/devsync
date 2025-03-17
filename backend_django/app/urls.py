from django.urls import path, include
from rest_framework import routers

from . import views
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api-root/', include(router.urls)),
    path('', views.index, name="index")
]