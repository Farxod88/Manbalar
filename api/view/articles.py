from django.views.generic import ListView
from rest_framework.generics import ListAPIView

from api.pagination import ResultsSetPagination
from articles.models import Articles
from articles.serializers import ArticlesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ArticlesListViews(ListAPIView):
    serializer_class = ArticlesSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Articles.objects.all()


@api_view(['GET'])

def articlesdetail(request, pk):
    articles = get_object_or_404(Articles, pk=pk)
    serializer = ArticlesSerializer(articles,  context={'request': request})
    return Response(serializer.data)