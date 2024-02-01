from rest_framework import serializers

from sliders.models import Sliders


class SlidersSerializer(serializers.Serializer):


    class Meta:
        model = Sliders
        fields = ('id', 'title', 'link', 'file', 'create', 'update')
