from rest_framework import serializers
from core.models import Post
from core.models import AppUser
from core.serializer.appuser_serializer import AppUserSerializer

class PostSerializer(serializers.ModelSerializer):
    sub = AppUserSerializer(read_only=True)
    sub_id = serializers.PrimaryKeyRelatedField(
        queryset=AppUser.objects.all(),
        write_only=True
    )

    class Meta:
        model = Post
        fields = ['id', 'comment', 'image', 'sub', 'sub_id']
        read_only_fields = ['created_at', 'updated_at']
