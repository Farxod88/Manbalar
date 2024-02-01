# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
# from ckeditor.fields import RichTextField




class Articles(models.Model):
    title = models.CharField(max_length=120)
    content = RichTextField(verbose_name='content')
    file = models.FileField(upload_to='files/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"