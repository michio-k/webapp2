from django.db import models
from core.models.app_user import AppUser
from core.models.post import Post

class Like(models.Model):
    sub = models.ForeignKey(AppUser,
        verbose_name="sub",
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(Post,
        verbose_name="post",
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        '作成日', auto_now_add=True, blank=True, null=True
    )
    updated_at = models.DateTimeField(
        '更新日', auto_now=True, blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = 'likes'
