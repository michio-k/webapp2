from django.shortcuts import render
from django.http import  HttpResponse

from rest_framework import viewsets, filters

from .models import User
from .serializer import UserSerializer
from .models import Post
from .serializer import PostSerializer

# Create your views here.
def index(request):
    return HttpResponse('Hello World')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
