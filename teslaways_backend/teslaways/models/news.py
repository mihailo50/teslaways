from django.db import models
from teslaways.models import zone



class News(models.Model):
    title = models.CharField(max_length=250, null=False)
    slug = models.SlugField(max_length=250, null=False)
    short_body = models.TextField(null=False)
    body = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)
    thumb_img = models.ImageField(upload_to='news/', blank=True, default='nophoto.jpg')
    zone = models.ForeignKey(zone.Zone,related_name='zone', on_delete=models.CASCADE)
    sort_positions = models.PositiveIntegerField(blank=True, null=True, unique=True)

    def __str__(self):
        return f"[{self.id}] {self.title}"

    class Meta:
        verbose_name = "Vest"
        verbose_name_plural = "Vesti"