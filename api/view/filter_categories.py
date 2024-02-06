from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from filter_categories.models import Filter_cotegory
from filter_categories.serializers import Filter_categoriesSerializer


class Filter_categoryListViews(ListAPIView):
    serializer_class = Filter_categoriesSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Filter_cotegory.objects.all()


@api_view(['GET'])

def filter_categoriesdetail(request, pk):
    filter_categories = get_object_or_404(Filter_cotegory, pk=pk)
    serializer = Filter_categoriesSerializer(filter_categories,  context={'request': request})
    return Response(serializer.data)