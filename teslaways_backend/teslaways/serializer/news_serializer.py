from random import choices
from rest_framework import serializers
from teslaways.models import destination, news, zone

class ViewZoneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = zone.Zone
        fields = ('name',)


class AllNewsSerializer(serializers.ModelSerializer):
    
#     zone = serializers.CharField(source='zone.name')

    class Meta:
        model = news.News
        fields = ('id', 'zone', 'title', 'thumb_img', 'short_body', 'sort_positions')
        # ordering = ('-sort_positions',)


class DetailNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = news.News
        fields = ('id', 'zone','title', 'thumb_img', 'body', 'short_body')


class ZonesForNewsSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = zone.Zone
        fields = ('name', )
