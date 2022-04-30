from rest_framework import serializers
from teslaways.models import baneri

class BaneriSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = baneri.Banana
        fields = ('id', 'image', 'active')