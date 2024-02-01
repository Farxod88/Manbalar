from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from categories.models import Categories
from categories.serializers import CategoriesSerializer


class CategoriesListViews(ListView):
    serializer_class = CategoriesSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Categories.objects.all()


@api_view(['GET'])

def categoriesdetail(request, pk):
    categories = get_object_or_404(Categories, pk=pk)
    serializer = CategoriesSerializer(categories, context={'request': request})
    return Response(serializer.data)