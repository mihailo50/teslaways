from teslaways.models import gallery
from teslaways_admin.serializers import managegallery
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser

class GalleryViewSet(viewsets.ModelViewSet):

    serializer_class = managegallery.ManageGallerySerializer
    parser_class = [FileUploadParser]
    queryset = gallery.Destination.objects.all()

