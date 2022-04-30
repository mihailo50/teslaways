from rest_framework import serializers
from teslaways.models import destination, gallery

class DestinationGallerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = gallery.DestinationGallery
        fields = ('id', 'image',)


class ManageDestinationSerializer(serializers.ModelSerializer):
    tip = serializers.MultipleChoiceField(choices=destination.MY_CHOICES)
    destinationgallery = DestinationGallerySerializer(many=True, required=False)
    class Meta:
        model = destination.Destination
        fields = ('id', 'title', 'address', 'short_body', 'body', 'lat', 'lng', 'thumb_img', 'zone', 'pod_tip',  'destinationgallery', 'tip', 'sort_positions')
        read_only_fields = ('destinationgallery',)