from teslaways.models import destination
from teslaways_admin.serializers import managedestination
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser

class DestinationViewSet(viewsets.ModelViewSet):
    
    serializer_class = managedestination.ManageDestinationSerializer
    parser_class = [FileUploadParser]
    queryset = destination.Destination.objects.all()

    

    # def retrieve(self, request, pk=None):
    #     queryset = destination.Destination.objects.all()
    #     destinations = get_object_or_404(queryset, pk=pk)
    #     serializer = managedestination.ManageDestinationSerializer(destinations)
    #     return Response(serializer.data)



    # def update(self, request, pk=None):
    #     queryset = destination.Destination.objects.all()
    #     destinations = get_object_or_404(queryset, pk=pk)
    #     serializer = managedestination.ManageDestinationSerializer(destinations, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)