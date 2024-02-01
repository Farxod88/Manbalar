from django.db import models

from categories.models import Categories
from filter_categories.models import Filter_cotegory
# from sources.models import BaseModel


class Filters(models.Model):
    select_category = models.ForeignKey(Filter_cotegory, on_delete=models.CASCADE, related_name='filter_category')
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Filter'
        verbose_name_plural = 'Filters'


