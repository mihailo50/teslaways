from rest_framework import viewsets
from rest_framework.response import Response
from teslaways.serializer import destination_serializer
from teslaways.models import destination, podtip, zone
from teslaways.filter import DestinationFilter, PodTipDestinationFilter
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse


class DestinationsViewSet(viewsets.ModelViewSet):

    serializer_class = destination_serializer.AllDestinationSerializer
    queryset = destination.Destination.objects.all()
    http_method_names = ['get']
    filterset_class = DestinationFilter

    def retrieve(self, request, pk=None):
        queryset = destination.Destination.objects.all()
        destinations = get_object_or_404(queryset, pk=pk)
        serializer = destination_serializer.DestinationDetailsSerializer(destinations)
        return Response(serializer.data)


class MapViewSet(viewsets.ModelViewSet):

    serializer_class = destination_serializer.PodTipsPartSerializer
    queryset = podtip.Podtip.objects.all()
    filterset_class = PodTipDestinationFilter
    pagination_class = None
    http_method_names = ['get']


    
class DestinatonsZones(viewsets.ModelViewSet):
    
    serializer_class = destination_serializer.ZonesForDestinacionsSerializer
    queryset = destination.Destination.objects.raw("SELECT DISTINCT tz.id, tz.name FROM teslaways_zone tz JOIN teslaways_destination td ON tz.id = td.zone_id")
    http_method_names = ['get']
    pagination_class = None

class DestinatonsPodTip(viewsets.ModelViewSet):
    
    serializer_class = destination_serializer.PodTipForDestinacionsSerializer
    #raw("SELECT DISTINCT pt.id, pt.name FROM teslaways_podtip pt JOIN teslaways_destination td ON pt.id = td.pod_tip_id")
    queryset = destination.Destination.objects.raw("SELECT DISTINCT pt.id, pt.name FROM teslaways_podtip pt JOIN teslaways_destination td ON pt.id = td.pod_tip_id")
    http_method_names = ['get']
    pagination_class = None

class DestinatonsTips(viewsets.ModelViewSet):
    
    serializer_class = destination_serializer.TipsForDestinacionsSerializer

    # queryset = destination.Destination.objects.raw("SELECT DISTINCT td.id,td.tip FROM teslaways_destination td")
    queryset = destination.Destination.objects.all()
    http_method_names = ['get']
    pagination_class = None

    def list(self, request):
        get_destinations = destination.Destination.objects.all().values()
        serializer = destination_serializer.TipsForDestinacionsSerializer(get_destinations, many=True)
        return Response(serializer.data)
