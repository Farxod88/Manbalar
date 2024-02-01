from rest_framework import serializers

from comments.models import Comments


class CommentsSerializer(serializers.Serializer):



    class Meta:
        model = Comments
        fields = ('id', 'massage', 'author_email',  'status', )