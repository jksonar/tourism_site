from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('my/', views.my_bookings, name='my_bookings'),
    path('package/<int:package_id>/book/', views.book_package, name='book_package'),
    path('success/', views.booking_success, name='booking_success'),  # Add this view
]
