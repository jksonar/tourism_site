from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from packages.models import TravelPackage
from .forms import BookingForm

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def book_package(request, package_id):
    package = get_object_or_404(TravelPackage, id=package_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.package = package
            booking.save()
            return redirect('booking_success')  # Define this URL
    else:
        form = BookingForm()

    return render(request, 'bookings/book_package.html', {
        'package': package,
        'form': form
    })

def booking_success(request):
    return render(request, 'bookings/booking_success.html')
