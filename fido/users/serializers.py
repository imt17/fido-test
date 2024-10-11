# serializers.py
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'name', 'age', 'friends']
        read_only_fields = ['id']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'age', 'friends', 'password']
