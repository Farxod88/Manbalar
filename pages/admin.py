from django.contrib import admin

from pages.models import Pages


# Register your models here.


class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')
    search_fields = ('title', 'content')
    list_filter = ('title', 'content')


admin.site.register(Pages, PagesAdmin)