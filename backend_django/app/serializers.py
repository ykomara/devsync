from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model=User
        fields=['id', 'username', 'email', 'is_staff']
