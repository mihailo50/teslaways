from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from teslaways.serializer import staticki_serializer
from teslaways.models import staticki


class StatickiViewSet(viewsets.ModelViewSet):

    serializer_class = staticki_serializer.StatickiSerializer
    queryset = staticki.Staticki.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']

    def retrieve(self, request, pk=None):
        queryset = staticki.Staticki.objects.all()
        statick = get_object_or_404(queryset, pk=pk)
        serializer = staticki_serializer.StatickiSerializer(statick)
        return Response(serializer.data)