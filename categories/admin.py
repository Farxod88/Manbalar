from django.contrib import admin

from categories.models import Categories


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('iconca', 'title', 'map', )
    list_display_links = ('title', 'map')
    list_filter = ('title',)



admin.site.register(Categories, CategoriesAdmin)