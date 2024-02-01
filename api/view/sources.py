from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from sources.models import Sources
from sources.serializers import SourcesSerializer


class SourcesListViews(ListView):
    serializer_class = SourcesSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Sources.objects.all()


@api_view(['GET'])

def sourcesdetail(request, pk):
    sources = get_object_or_404(Sources, pk=pk)
    serializer = SourcesSerializer(sources,  context={'request': request})
    return Response(serializer.data)