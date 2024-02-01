from rest_framework import serializers



class FiltersSerializer(serializers.Serializer):


    class Meta:
        model = 'Filters'
        fields = ('id', 'category', 'title', 'select_category',)



