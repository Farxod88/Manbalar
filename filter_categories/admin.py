from django.contrib import admin

from filter_categories.models import Filter_cotegory


class Filter_categoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title',)
    list_per_page = 10





admin.site.register(Filter_cotegory, Filter_categoryAdmin)
