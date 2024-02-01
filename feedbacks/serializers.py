from rest_framework import serializers

from feedbacks.models import Feedbacks


class FeedbacksSerializer(serializers.Serializer):



    class Meta:
        model = Feedbacks
        fields = ('id', 'user', 'massage')


