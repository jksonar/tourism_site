from django.urls import path
from . import views

urlpatterns = [
    path('destination/<int:pk>/add/', views.add_destination_review, name='add_destination_review'),
]
