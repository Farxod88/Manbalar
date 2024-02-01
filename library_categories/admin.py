from django.contrib import admin

from library_categories.models import Library_categories


class Library_categoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 25
    list_filter = ('title',)




admin.site.register(Library_categories, Library_categoriesAdmin)