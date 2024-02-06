from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from library_categories.models import Library_categories
from library_categories.serializers import Library_categoriesSerializer


class Library_categoriesListViews(ListAPIView):
    serializer_class = Library_categoriesSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Library_categories.objects.all()


@api_view(['GET'])

def library_categoriesdetail(request, pk):
    library_categories = get_object_or_404(Library_categories, pk=pk)
    serializer = Library_categoriesSerializer(library_categories,  context={'request': request})
    return Response(serializer.data)