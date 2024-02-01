from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from comments.models import Comments
from comments.serializers import CommentsSerializer


class CommentsListViews(ListView):
    serializer_class = CommentsSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Comments.objects.all()


@api_view(['GET'])

def commentsdetail(request, pk):
    comments = get_object_or_404(Comments, pk=pk)
    serializer = CommentsSerializer(comments, context={'request': request})
    return Response(serializer.data)