# coding: utf-8
from rest_framework import serializers
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'date_of_birth', 'is_active', 'is_admin')
