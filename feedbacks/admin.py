from django.contrib import admin

from feedbacks.models import Feedbacks


class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('message', 'user',)
    search_fields = ('message', 'user',)
    list_per_page = 25


    class Meta:
        model = Feedbacks
        fields = ('message',)

admin.site.register(Feedbacks, FeedbacksAdmin)