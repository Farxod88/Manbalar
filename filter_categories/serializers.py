from rest_framework import serializers



class Filter_categoriesSerializer(serializers.Serializer):



    class Meta:
        model = 'Filter_categories'
        fields = ('id', 'title', 'category')

