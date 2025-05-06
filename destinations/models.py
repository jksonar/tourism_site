from reviews.models import Review  # optionally for type hinting
from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    best_time_to_visit = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def reviews(self):
        from django.contrib.contenttypes.models import ContentType
        content_type = ContentType.objects.get_for_model(self)
        return Review.objects.filter(content_type=content_type, object_id=self.id)
