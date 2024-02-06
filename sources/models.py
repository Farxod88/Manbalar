# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import TextField

from categories.models import Categories
from filter_categories.models import Filter_cotegory
from filters.models import Filters
from period_filter.models import Period_filter
from django.contrib.contenttypes.models import ContentType


class Province(models.Model):
    province_name = models.CharField(max_length=100, verbose_name='Province')

    def __str__(self):
        return self.province_name


class ItemBase(models.Model):
    title = models.CharField(max_length=100)
    count = models.IntegerField(auto_created=True, default=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Gallery(ItemBase):
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.image.name


class Audios(ItemBase):
    audio = models.FileField(upload_to='audios')

    def __str__(self):
        return self.audio.name


class Videos(ItemBase):
    video = models.FileField(upload_to='videos')

    def __str__(self):
        return self.video.name


class Files(ItemBase):
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.file.name


class Location(ItemBase):
    location_name = models.CharField(max_length=100, verbose_name='Location')

    def __str__(self):
        return self.location_name


class Vertual_reality(ItemBase):
    vr = models.FileField(upload_to='vr')

    def __str__(self):
        return self.vr.name

# class Select_filter(models.Model):
#     category_filter = models.ForeignKey(Filter_cotegory, on_delete=models.CASCADE, null=True,
#                                         verbose_name='Select a filter ', help_text='Select a filter ', max_length=100, )




class Sources(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Select a category',
                                 help_text='Select a category', max_length=100, )
    select_filter = models.ForeignKey(Filter_cotegory, on_delete=models.CASCADE, verbose_name ='Select a filter category',
                                      help_text='Select a filter category', max_length=100, )
    category_filter = models.OneToOneField(Filters, on_delete=models.CASCADE, null=True, verbose_name='Select a filter',)
    period_filter = models.ForeignKey(Period_filter, on_delete=models.CASCADE, null=True,
                                      verbose_name='Select a period filter', help_text='Select a period filter',
                                      max_length=100, )
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='sources', null=True, blank=True, verbose_name='Click to upload an image',
                            help_text='Click to upload an image', max_length=100, )
    content = TextField()
    statehood = models.BooleanField(default=False, verbose_name='Statehood', )
    # atributes = models.TextField()
    # contents = models.TextField()
    # interive_contents = models.ForeignKey(
    #     ContentType,
    #     on_delete=models.CASCADE,
    #     limit_choices_to={'model__in': ('audios', 'videos', 'gallery', 'files', 'location', 'vertual_reality')}
    # )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Interive_contents(models.Model):
    interive_contents_set = models.ForeignKey(Sources, on_delete=models.CASCADE, related_name='interive_set', verbose_name='Interive contents',)
    interive_contents = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('audios', 'videos', 'gallery', 'files', 'location', 'vertual_reality')}
    )
    title = models.CharField(max_length=255)
    count = models.IntegerField(auto_created=True, default=1)
    file = models.FileField(upload_to='interive_contents', verbose_name='Interive file',)

    def __str__(self):
        return self.title


class Atribute(models.Model):
    count = models.IntegerField(auto_created=True, default=1)
    atribute = models.ForeignKey(Sources, on_delete=models.CASCADE, verbose_name='Atributes', help_text='Atributes',
                                 max_length=100, )
    title = models.CharField(max_length=255, verbose_name='Atribute title', help_text='Atribute title', )
    description = models.CharField(max_length=255,  verbose_name='Atribute description', help_text='Atribute description', )


    def __str__(self):
        return self.title


class Contents(models.Model):
    contents = models.ForeignKey(Sources, on_delete=models.CASCADE, related_name='content_set', verbose_name='Contents',
                                 help_text='Contents', max_length=100, )
    title = models.CharField(max_length=255,  verbose_name='Content title', help_text='Content title', )
    count = models.IntegerField(auto_created=True, default=1)
    text = TextField(verbose_name='')

    def __str__(self):
        return self.title

# from django.contrib.contenttypes.models import ContentType
# from django.db import models
# # from .models import ItemBase
# from categories.models import Categories
# from filter_categories.models import Filter_cotegory
# from filters.models import Filters
# from period_filter.models import Period_filter
#
#
#
# class Sources(models.Model):
#     category = models.ForeignKey(Categories, on_delete=models.CASCADE)
#     select_filter = models.ForeignKey(Filters, on_delete=models.CASCADE)
#     category_filter = models.ForeignKey(Filter_cotegory, on_delete=models.CASCADE, null=True)
#     period_filter = models.ForeignKey(Period_filter, on_delete=models.CASCADE, null=True)
#     title = models.CharField(max_length=255)
#     file = models.FileField(upload_to='sources')
#     content = models.TextField()
#     statehood = models.BooleanField(default=False)
#     atributes = models.TextField()
#     contents = models.TextField()
#     interive_contents = models.ForeignKey(ContentType, on_delete=models.CASCADE,
#                                           limit_choices_to={'model_in': (
#                                           'audio', 'video', 'gallery', 'file', 'location', 'vertual_reality')})
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
# class ItemBase(models.Model):
#     title = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         abstract = True
#
# class Gallery(ItemBase):
#     image = models.ImageField(upload_to='gallery')
#
#     def __str__(self):
#         return self.image
#
# class Audios(ItemBase):
#     audio = models.FileField(upload_to='audios')
#
#     def __str__(self):
#         return self.audio.name
#
# class Videos(ItemBase):
#     video = models.FileField(upload_to='videos')
#
#     def __str__(self):
#         return self.video.name
#
# class Files(ItemBase):
#     file = models.FileField(upload_to='files')
#
#     def __str__(self):
#         return self.file.name
#
# class Location(ItemBase):
#     location_name = models.CharField(max_length=100, verbose_name='Location')
#
#     def __str__(self):
#         return self.location_name
#
# class Vertual_reality(ItemBase):
#     vr = models.FileField(upload_to='vr')
#
#     def __str__(self):
#         return self.vr.name
#
# def __str__(self):
#     return self.title
#
#
#
#
#
#
#
#
#
#
#
