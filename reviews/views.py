from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, render, get_object_or_404
from .models import Review
from .forms import ReviewForm
from destinations.models import Destination

def add_destination_review(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    content_type = ContentType.objects.get_for_model(destination)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.content_type = content_type
            review.object_id = destination.id
            review.save()
            return redirect('destination_detail', pk=destination.pk)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {
        'form': form,
        'object': destination
    })
