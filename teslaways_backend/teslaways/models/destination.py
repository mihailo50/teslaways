from django.db import models
from multiselectfield import MultiSelectField
from teslaways.models import zone, podtip


MY_CHOICES = (('jesti', 'jesti'),
              ('spavati', 'spavati'),
              ('videti', 'videti'))



class Destination(models.Model):
    title = models.CharField(max_length=250, null=False)
    address = models.CharField(max_length=100, null=False)
    short_body = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=False)
    body = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)
    lat = models.FloatField(null=False)
    lng = models.FloatField(null=False)
    thumb_img = models.ImageField(upload_to='destination/', blank=True, default='nophoto.jpg')
    zone = models.ForeignKey(zone.Zone, on_delete=models.CASCADE)
    pod_tip = models.ForeignKey(podtip.Podtip, related_name='destinations', on_delete=models.CASCADE)
    tip = MultiSelectField(choices=MY_CHOICES)
    sort_positions = models.PositiveIntegerField(blank=True, null=True, unique=True)

    def __str__(self):
        return f"[{self.id}] {self.title} - {self.address} - {self.pod_tip}"


    class Meta:
        verbose_name = "Destinacija"
        verbose_name_plural = "Destinacije"