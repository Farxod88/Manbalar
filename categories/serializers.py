from rest_framework import serializers

from categories.models import Categories


class CategoriesSerializer(serializers.Serializer):



    class Meta:
        model = Categories
        fields = ('id', 'title', 'iconca', 'map')