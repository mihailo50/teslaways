from rest_framework.response import Response
from rest_framework import viewsets
from teslaways.serializer import destination_serializer, news_serializer
from teslaways.models import destination, news, podtip, zone
from django.shortcuts import get_object_or_404
from teslaways.filter import NewsFilter

class NewsViewSet(viewsets.ModelViewSet):

    serializer_class = news_serializer.AllNewsSerializer
    queryset = news.News.objects.all().order_by('sort_positions')
    http_method_names = ['get']
    filterset_class = NewsFilter

    def retrieve(self, request, pk=None):
        queryset = news.News.objects.all()
        new = get_object_or_404(queryset, pk=pk)
        serializer = news_serializer.DetailNewsSerializer(new)
        return Response(serializer.data)

class NewsZones(viewsets.ModelViewSet):
    
    serializer_class = news_serializer.ZonesForNewsSerializer
    queryset = news.News.objects.all()
    http_method_names = ['get']
    pagination_class = None


class PocetnaStranica(viewsets.ModelViewSet):
         
    serializer_class = news_serializer.AllNewsSerializer
    queryset = news.News.objects.all()
    http_method_names = ['get']
    pagination_class = None

    def list(self, request):
        all_news = news.News.objects.all()
        all_destinations = destination.Destination.objects.all()
        all_podtips = podtip.Podtip.objects.all()
        serializer_news = news_serializer.AllNewsSerializer(all_news, many=True).data
        serializer_destinations = destination_serializer.AllDestinationSerializer(all_destinations, many=True).data
        serializer_podtips = destination_serializer.PodTipsPartSerializer(all_podtips, many=True).data
        serializer_zone_news = news_serializer.ZonesForNewsSerializer(all_news, many=True).data
        return Response({
            'News': serializer_news,
            'Destinations': serializer_destinations,
            'Map destinations': serializer_podtips,
            'Zones in news': serializer_zone_news
        })        
    

    
class NewsZones(viewsets.ModelViewSet):
    
    serializer_class = news_serializer.ZonesForNewsSerializer
    queryset = news.News.objects.raw("SELECT DISTINCT tz.id, tz.name FROM teslaways_zone tz JOIN teslaways_news tn ON tz.id = tn.zone_id")
    http_method_names = ['get']
    pagination_class = None


