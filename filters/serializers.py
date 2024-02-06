from rest_framework import serializers



class FiltersSerializer(serializers.ModelSerializer):


    class Meta:
        model = 'Filters'
        fields = ('id', 'category', 'title', 'select_category',)



