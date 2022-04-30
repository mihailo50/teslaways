from rest_framework import serializers
from teslaways.models import staticki

class StatickiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = staticki.Staticki
        fields = ('id','title' ,'text', 'phone')