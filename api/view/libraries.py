from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from libraries.models import Libraries
from libraries.serializers import LibrariesSerializer


class LibrariesListViews(ListView):
    serializer_class = LibrariesSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Libraries.objects.all()


@api_view(['GET'])

def librariesdetail(request, pk):
    libraries = get_object_or_404(Libraries, pk=pk)
    serializer = LibrariesSerializer(libraries,  context={'request': request})
    return Response(serializer.data)