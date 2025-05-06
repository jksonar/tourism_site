from django.contrib import admin
from .models import TravelPackage

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'duration_days', 'price')
    search_fields = ('title', 'destination__name')
    list_filter = ('destination',)
