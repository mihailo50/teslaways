from rest_framework import serializers
from teslaways.models import zone

class ManageZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = zone.Zone
        fields = ('name','id')