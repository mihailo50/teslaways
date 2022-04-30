from teslaways.models import podtip
from teslaways_admin.serializers import managepodtip
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser, MultiPartParser

class PodTipViewSet(viewsets.ModelViewSet):

    serializer_class = managepodtip.ManagePodTipSerializer
    parser_class = [FileUploadParser, MultiPartParser]
    queryset = podtip.Podtip.objects.all()