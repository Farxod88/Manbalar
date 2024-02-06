from rest_framework import serializers

from feedbacks.models import Feedbacks


class FeedbacksSerializer(serializers.ModelSerializer):



    class Meta:
        model = Feedbacks
        fields = ('id', 'user', 'message')


