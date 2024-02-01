from django.db import models

# from sources.models import BaseModel


class Categories(models.Model):
    title = models.CharField(max_length=50)
    iconca = models.FileField(upload_to='icons/')
    map = models.BooleanField(default=False,  verbose_name='Map')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_icon(self):
            return self.iconca

    def get_map(self):
            return self.map

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'
