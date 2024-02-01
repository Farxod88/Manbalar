from rest_framework import serializers

from sources.models import Sources


class SourcesSerializer(serializers.Serializer):



    class Meta:
        model = Sources
        fields = ('id', 'category',  'select_filter', 'category_filter', 'period_filter', 'title', 'file', 'content', 'statehood', 'atributes', 'contents', 'interive_contents',)