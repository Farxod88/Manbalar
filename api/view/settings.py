from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.pagination import ResultsSetPagination
from settings.models import Settings
from settings.serializers import SettingsSerializer


class SettingsListViews(ListView):
    serializer_class = SettingsSerializer
    pogination_class = ResultsSetPagination

    def get_queryset(self):
        return Settings.objects.all()


@api_view(['GET'])

def settingsdetail(request, pk):
    settings = get_object_or_404(Settings, pk=pk)
    serializer = SettingsSerializer(settings,  context={'request': request})
    return Response(serializer.data)