from rest_framework import serializers
from teslaways.models import news

class ManageNewsSerializer(serializers.ModelSerializer):

    #zone = serializers.CharField(source='zone.name')

    class Meta:
        model = news.News
        fields = ('id','title', 'short_body', 'body', 'thumb_img', 'zone', 'sort_positions')
        