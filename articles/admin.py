from django.contrib import admin

from articles.models import Articles


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'file',)
    list_filter = ("title", 'file' )
    search_fields = ['title', 'content']




admin.site.register(Articles, ArticlesAdmin)