from django.db import models

from categories.models import Categories
# from sources.models import BaseModel


class Filter_cotegory(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Filter_cotegory'
        verbose_name_plural = 'Filter_cotegory'