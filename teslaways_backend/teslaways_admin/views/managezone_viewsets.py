from teslaways.models import zone
from teslaways_admin.serializers import managezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class ZoneViewSet(viewsets.ModelViewSet):

    serializer_class = managezone.ManageZoneSerializer
    queryset = zone.Zone.objects.all()
    
        
        