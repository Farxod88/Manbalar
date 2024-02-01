from django.contrib import admin

from comments.models import Comments


# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = [ 'massage', 'status', ]
    list_filter = ['status', ]
    fields = [ 'massage', 'status',]





admin.site.register(Comments, CommentAdmin)