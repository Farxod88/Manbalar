from django.contrib import admin

from period_filter.models import Period_filter


class Period_filterAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


    # class Meta:
    #     model = Period_filter
    #     fields = ['title', 'created_at', 'updated_at']



admin.site.register(Period_filter,  Period_filterAdmin)