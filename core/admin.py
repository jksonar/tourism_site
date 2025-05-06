# OLD (wrong)
# from .models import Destination, TourPackage, Booking

# ✅ NEW (correct)
from .models import ContactMessage

from django.contrib import admin

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
