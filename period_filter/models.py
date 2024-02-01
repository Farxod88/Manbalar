from django.db import models

# from sources.models import BaseModel


class Period_filter(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Period_filter'
        verbose_name_plural = 'Period_filter'
        ordering = ['title']
