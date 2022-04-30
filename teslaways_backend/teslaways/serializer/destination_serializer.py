from dataclasses import field
from rest_framework import serializers
from teslaways.models import destination, podtip, gallery, zone

class DestinationGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = gallery.DestinationGallery
        fields = ('image',)

class AllDestinationSerializer(serializers.ModelSerializer):

    zone = serializers.CharField(source='zone.name')
    pod_tip = serializers.CharField(source='pod_tip.name')
    destinationgallery = DestinationGallerySerializer(many=True, read_only=True)
    
    class Meta:
        model = destination.Destination
        fields = ('id', 'zone', 'title', 'thumb_img', 'short_body', 'body', 'sort_positions', 'tip', 'pod_tip','lat', 'lng', 'destinationgallery')
        

class DestinationDetailsSerializer(serializers.ModelSerializer):

    destinationgallery = DestinationGallerySerializer(many=True, read_only=True)

    class Meta:
        model = destination.Destination
        fields = ('id', 'title', 'zone', 'body', 'pod_tip', 'tip', 'address', 'lat', 'lng', 'destinationgallery')
        depth = 1

class PodTipsDestinationsSerializer(serializers.ModelSerializer): #1

    zone = serializers.CharField(source='zone.name')

    class Meta:
        model = destination.Destination
        fields = ('id', 'title', 'zone', 'address', 'sort_positions', 'lat', 'lng')

# map

class DestinationsPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = destination.Destination
        fields = ('id', 'title', 'zone', 'tip', 'address', 'lat', 'lng')
        
class PodTipsPartSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        podtip_structure = {}
        podtip_structure['id'] = instance.id
        podtip_structure['icon'] = f"{instance.icon}"
        query = destination.Destination.objects.filter(pod_tip__name=instance.name)
        destinations = DestinationsPartSerializer(query, many=True).data
        podtip_structure['destinations'] = destinations

        data = {instance.name: podtip_structure}

        return data

    class Meta:
        model = podtip.Podtip
        fields = ('name', 'icon', 'destinations')


class ZonesForDestinacionsSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = zone.Zone
        fields = ('name', )

class PodTipForDestinacionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = podtip.Podtip
        fields = ('name',)

class TipsForDestinacionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = destination.Destination
        fields = ('tip',)