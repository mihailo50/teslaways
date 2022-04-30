from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from teslaways.serializer import slajder_serializer
from teslaways.models import slajder


class SlajderViewSet(viewsets.ModelViewSet):

    serializer_class = slajder_serializer.SlajderSerializer
    queryset = slajder.Slajder.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']

    def retrieve(self, request, pk=None):
        queryset = slajder.Slajder.objects.all()
        slajderi = get_object_or_404(queryset, pk=pk)
        serializer = slajder_serializer.SlajderSerializer(slajderi)
        return Response(serializer.data)