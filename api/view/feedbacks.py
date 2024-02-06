from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from feedbacks.models import Feedbacks
from feedbacks.serializers import FeedbacksSerializer


class FeedbacksListViews(ListAPIView):
    serializer_class = FeedbacksSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Feedbacks.objects.all()


@api_view(['GET'])

def feedbacksdetail(request, pk):
    feedbacks = get_object_or_404(Feedbacks, pk=pk)
    serializer = FeedbacksSerializer(feedbacks,  context={'request': request})
    return Response(serializer.data)