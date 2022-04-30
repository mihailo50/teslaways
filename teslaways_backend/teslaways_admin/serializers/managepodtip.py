from rest_framework import serializers
from teslaways.models import podtip

class ManagePodTipSerializer(serializers.ModelSerializer):

    class Meta:
        model = podtip.Podtip
        fields = ('id', 'name', 'icon')

class UpdatePodTipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = podtip.Podtip
        fields = ('id', 'name', 'icon')
        read_only_fields=('icon',)