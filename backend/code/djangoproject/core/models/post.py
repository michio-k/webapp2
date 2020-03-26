from django.db import models
from core.models.app_user import AppUser

class Post(models.Model):
    sub = models.ForeignKey(AppUser,
        verbose_name='sub',
        on_delete=models.CASCADE
    )

    comment = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    created_at = models.DateTimeField(
        '作成日', auto_now_add=True, blank=True, null=True
    )
    updated_at = models.DateTimeField(
        '更新日', auto_now=True, blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = 'post'

    def __str__(self):
        return self.comment
