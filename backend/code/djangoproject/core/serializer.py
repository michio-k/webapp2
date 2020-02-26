# coding: utf-8
from rest_framework import serializers
from .models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'date_of_birth', 'is_active', 'is_admin')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =('comment', 'image')
