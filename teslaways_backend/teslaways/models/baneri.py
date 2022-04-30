from django.db import models


class Banana(models.Model):
    image = models.ImageField(upload_to='baneri', blank=True)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Baner id: {self.id}, slika: {self.image}"

    class Meta:
        verbose_name = "Baner"
        verbose_name_plural = "Baneri"