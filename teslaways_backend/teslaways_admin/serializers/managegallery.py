from rest_framework import serializers
from teslaways.models import gallery

class ManageGallerySerializer(serializers. ModelSerializer):

    class Meta:
        model = gallery.DestinationGallery
        fields = ('id', 'image', 'destinations')