from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from period_filter.models import Period_filter
from period_filter.serializers import Period_filterSerializer


class Period_filterListViews(ListView):
    serializer_class = Period_filterSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Period_filter.objects.all()


@api_view(['GET'])

def period_filterdetail(request, pk):
    period_filter = get_object_or_404(Period_filter, pk=pk)
    serializer = Period_filterSerializer(period_filter,  context={'request': request})
    return Response(serializer.data)