from django.db import models

# from sources.models import BaseModel




class Comments(models.Model):
    massage = models.TextField()
    # author_email = models.EmailField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.massage

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-id"]