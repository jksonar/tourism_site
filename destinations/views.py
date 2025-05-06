from django.shortcuts import render, get_object_or_404
from .models import Destination
from django.db.models import Q
from django.core.paginator import Paginator


def destination_list(request):
    query = request.GET.get('q', '')
    best_time = request.GET.get('best_time', '')
    page_number = request.GET.get('page', 1)

    destinations = Destination.objects.all()

    if query:
        destinations = destinations.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query)
        )

    if best_time:
        destinations = destinations.filter(best_time_to_visit__icontains=best_time)

    paginator = Paginator(destinations, 6)  # Show 6 destinations per page
    page_obj = paginator.get_page(page_number)

    best_times = Destination.objects.values_list('best_time_to_visit', flat=True).distinct()

    context = {
        'page_obj': page_obj,
        'query': query,
        'best_time': best_time,
        'best_times': best_times,
    }

    return render(request, 'destinations/list.html', context)

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'destinations/detail.html', {'destination': destination})