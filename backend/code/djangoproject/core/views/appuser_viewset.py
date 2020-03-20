from rest_framework import viewsets, filters

from core.models.app_user import AppUser
from core.serializer.appuser_serializer import AppUserSerializer

class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
