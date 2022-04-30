from django.db import models


class Slajder(models.Model):
    image = models.ImageField(upload_to='baneri', blank=True)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Slajder id: {self.id}, slika: {self.image}"

    class Meta:
        verbose_name = "Slajder"
        verbose_name_plural = "Slajderi"