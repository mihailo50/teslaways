from django.db import models

class Zone(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zone"