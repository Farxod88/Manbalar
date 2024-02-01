from django.contrib import admin

from libraries.models import Libraries


class LibrariesAdmin(admin.ModelAdmin):
    list_display = ('library_categories', 'title', 'author', 'type', 'year', 'country', 'language', 'image', 'file')
    list_filter = ('library_categories', 'type', 'year', 'country', 'language')
    search_fields = ('title', 'author')
    list_per_page = 25
    list_editable = ('image', 'file')
    list_display_links = ('title',)



admin.site.register(Libraries, LibrariesAdmin)