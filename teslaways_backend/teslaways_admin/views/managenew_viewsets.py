from teslaways.models import news
from teslaways_admin.serializers import managenew
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser

class NewsViewSet(viewsets.ModelViewSet):

    serializer_class = managenew.ManageNewsSerializer
    parser_class = [FileUploadParser]
    queryset = news.News.objects.all()