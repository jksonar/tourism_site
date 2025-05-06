from django.db import models
from destinations.models import Destination

class GalleryImage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
