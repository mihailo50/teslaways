from django.db import models

class Podtip(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icon/', blank=True, default='nophoto.jpg')
    map_show = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Podtip"
        verbose_name_plural = "Podtipovi"