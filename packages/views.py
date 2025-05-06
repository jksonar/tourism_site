from django.shortcuts import render, get_object_or_404
from .models import TravelPackage

def package_list(request):
    packages = TravelPackage.objects.all()
    return render(request, 'packages/list.html', {'packages': packages})

def package_detail(request, pk):
    package = get_object_or_404(TravelPackage, pk=pk)
    return render(request, 'packages/detail.html', {'package': package})
