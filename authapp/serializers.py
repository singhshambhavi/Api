from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers
from .models import *
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'dob')