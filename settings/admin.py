from django.contrib import admin

from settings.models import Settings


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('select_key', 'value')
    search_fields = ('select_key',)
    ordering = ('select_key',)
    list_filter = ('select_key',)
    list_per_page = 25
    list_max_show_all = 100



admin.site.register(Settings, SettingsAdmin)
