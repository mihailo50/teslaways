from rest_framework import serializers
from teslaways.models import slajder

class SlajderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = slajder.Slajder
        fields = ('id', 'image', 'active')