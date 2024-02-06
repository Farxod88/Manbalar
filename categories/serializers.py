from rest_framework import serializers

from categories.models import Categories


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ('id', 'title', 'iconca', 'map')


    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            data['files'] = [{'file': img.file.url} for img in files]

        return data