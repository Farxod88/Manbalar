from django.contrib.auth.models import User
from django.db import models

# from django.contrib.auth.models import User

# from sources.models import BaseModel


class Feedbacks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()


    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"