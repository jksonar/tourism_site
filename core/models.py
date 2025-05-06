from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    best_time_to_visit = models.CharField(max_length=100)
    activities = models.TextField()

    def __str__(self):
        return self.name

class TourPackage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    booking_date = models.DateField(auto_now_add=True)
    travel_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.package.title}"
