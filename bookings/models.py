# from django.db import models
# from django.contrib.auth.models import User
# from packages.models import TravelPackage  # Assuming packages app has TourPackage model

# class Booking(models.Model):
#     STATUS_CHOICES = (
#         ('pending', 'Pending'),
#         ('confirmed', 'Confirmed'),
#         ('cancelled', 'Cancelled'),
#     )

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
#     num_people = models.PositiveIntegerField()
#     booking_date = models.DateField()
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.package.title} ({self.status})"
    
from django.db import models
from django.contrib.auth.models import User
from packages.models import TravelPackage

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    travel_date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.package.title}"
