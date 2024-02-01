from django.db import models

# from sources.models import BaseModel


class Settings(models.Model):
    select_key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.select_key


    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'
        ordering = ['select_key']