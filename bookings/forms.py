from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['package', 'num_people', 'booking_date']
        widgets = {
            'booking_date': forms.SelectDateWidget()
        }
