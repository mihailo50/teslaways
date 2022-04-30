from django.db import models
from .destination import Destination

class DestinationGallery(models.Model):
    destinations = models.ForeignKey(Destination, related_name='destinationgallery', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='gallery-destination', blank=True, default='nophoto.jpg')

    class Meta:
        verbose_name = "Galerija za destinacije"
        verbose_name_plural = verbose_name