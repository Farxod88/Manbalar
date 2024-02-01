from rest_framework import serializers

from library_categories.models import Library_categories


class Library_categoriesSerializer(serializers.Serializer):


    class Meta:
        model = Library_categories
        fields = ('id', 'title',)


