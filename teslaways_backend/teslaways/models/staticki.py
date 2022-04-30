from pyexpat import model
from django.db import models


class Staticki(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    phone = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"[{self.id}] Staticki deo"

    class Meta:
        verbose_name = "Staticka stranica"
        verbose_name_plural = "Staticke stranice"