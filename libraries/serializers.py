from rest_framework import serializers

from libraries.models import Libraries


class LibrariesSerializer(serializers.Serializer):



    class Meta:
        model = Libraries
        fields = ('id', 'library_category', 'title', 'author', 'type', 'year', 'country', 'language', 'image', 'file')