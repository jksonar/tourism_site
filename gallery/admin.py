from django.contrib import admin
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'uploaded_at')
    list_filter = ('destination',)
    search_fields = ('title',)
