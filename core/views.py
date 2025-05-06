from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def faq(request):
    return render(request, 'core/faq.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_thanks')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def contact_thanks(request):
    return render(request, 'core/contact_thanks.html')
