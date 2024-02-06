from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from filters.models import Filters
from filters.serializers import FiltersSerializer


class FiltersListViews(ListAPIView):
    serializer_class = FiltersSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Filters.objects.all()


@api_view(['GET'])

def filtersdetail(request, pk):
    filters = get_object_or_404(Filters, pk=pk)
    serializer = FiltersSerializer(filters,  context={'request': request})
    return Response(serializer.data)