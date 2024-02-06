from rest_framework import serializers

from period_filter.models import Period_filter


class Period_filterSerializer(serializers.ModelSerializer):



    class Meta:
        model = Period_filter
        fields = ('id','name','start_date','end_date')