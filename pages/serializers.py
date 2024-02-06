from rest_framework import serializers

from pages.models import Pages


class PagesSerializer(serializers.ModelSerializer):


    class Meta:
        model = Pages
        fields = ('id', 'title', 'content', 'image', 'created_at', 'updated_at', )