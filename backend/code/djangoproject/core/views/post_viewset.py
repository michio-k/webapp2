from rest_framework import viewsets, filters

from core.models.post import Post
from core.serializer.post_serializer import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        sub_id = self.request.query_params.get('sub_id')
        return Post.objects.all().filter(sub_id=sub_id)
