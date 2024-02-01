from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from sliders.models import Sliders
from sliders.serializers import SlidersSerializer


class SlidersListViews(ListView):
    serializer_class = SlidersSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Sliders.objects.all()


@api_view(['GET'])

def slidersdetail(request, pk):
    sliders = get_object_or_404(Sliders, pk=pk)
    serializer = SlidersSerializer(sliders,  context={'request': request})
    return Response(serializer.data)