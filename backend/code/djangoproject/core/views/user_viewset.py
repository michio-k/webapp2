from rest_framework import viewsets, filters

from core.models.user import User
from core.serializer.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
