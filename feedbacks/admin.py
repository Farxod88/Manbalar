from django.contrib import admin

from feedbacks.models import Feedbacks


class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('message',)
    search_fields = ('massage',)
    list_per_page = 25


    class Meta:
        model = Feedbacks
        fields = ('user', 'massage',)

admin.site.register(Feedbacks, FeedbacksAdmin)