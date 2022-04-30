from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from teslaways.serializer import baneri_serializer
from teslaways.models import baneri


class BaneriViewSet(viewsets.ModelViewSet):

    serializer_class = baneri_serializer.BaneriSerializer
    queryset = baneri.Banana.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']

    def retrieve(self, request, pk=None):
        queryset = baneri.Banana.objects.all()
        baner = get_object_or_404(queryset, pk=pk)
        serializer = baneri_serializer.BaneriSerializer(baner)
        return Response(serializer.data)