from django.db import models

# from sources.models import BaseModel



class Sliders(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    file = models.FileField(upload_to='slider/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"