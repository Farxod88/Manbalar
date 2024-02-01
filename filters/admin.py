from django.contrib import admin

from filters.models import Filters


class FiltersAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'select_category',)
    list_display_links = ('category', 'title',)
    search_fields = ('category', 'title',)
    list_per_page = 25


    class Meta:
        model = Filters
        fields = ('category', 'select_category', 'title',)




admin.site.register(Filters, FiltersAdmin)