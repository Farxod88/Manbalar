from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from pages.models import Pages
from pages.serializers import PagesSerializer


class PagesListViews(ListAPIView):
    serializer_class = PagesSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Pages.objects.all()


@api_view(['GET'])

def pagesdetail(request, pk):
    pages = get_object_or_404(Pages, pk=pk)
    serializer = PagesSerializer(pages,  context={'request': request})
    return Response(serializer.data)