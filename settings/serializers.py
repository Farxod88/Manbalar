from rest_framework import serializers

from settings.models import Settings


class SettingsSerializer(serializers.Serializer):


    class Meta:
        model = Settings
        exclude = ('id',)
        fields = ('id', 'select_key', 'value')