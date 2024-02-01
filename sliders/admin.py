from django.contrib import admin

from sliders.models import Sliders


# Register your models here.


class SlidersAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'file',)
    list_filter = ( 'title', 'link',)
    search_fields = ('title', 'link', 'file')
    # ordering = ('-created_at',)




admin.site.register(Sliders, SlidersAdmin)