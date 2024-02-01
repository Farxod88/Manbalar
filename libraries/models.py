from django.db import models

from library_categories.models import Library_categories


# from sources.models import BaseModel




class Libraries(models.Model):
    library_categories = models.ForeignKey(Library_categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Libraries'
