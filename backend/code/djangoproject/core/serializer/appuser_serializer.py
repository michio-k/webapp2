from rest_framework import serializers
from core.models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['sub']
        read_only_fields = ['created_at', 'updated_at']
