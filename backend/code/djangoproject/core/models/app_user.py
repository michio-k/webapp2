from django.db import models

class AppUser(models.Model):
    sub = models.CharField(max_length=10000, primary_key=True)

    created_at = models.DateTimeField(
        '作成日', auto_now_add=True, blank=True, null=True
    )
    updated_at = models.DateTimeField(
        '更新日', auto_now=True, blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = 'appuser'

    def __str__(self):
        return self.sub
