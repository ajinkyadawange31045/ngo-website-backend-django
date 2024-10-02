# your_app/urls.py
from django.urls import path
from .views import donation_items, view_cart, add_to_cart

urlpatterns = [
    path('donation-items/', donation_items, name='donation_items'),
    path('view-cart/', view_cart, name='view_cart'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),  # Make sure this is included
]
