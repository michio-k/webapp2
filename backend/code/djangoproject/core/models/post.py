from django.db import models

class Post(models.Model):
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
