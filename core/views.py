from django.shortcuts import render
from .models import Destination, TourPackage

def home(request):
    destinations = Destination.objects.all()
    return render(request, 'core/home.html', {'destinations': destinations})
