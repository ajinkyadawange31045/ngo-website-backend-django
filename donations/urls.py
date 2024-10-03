# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('donation-confirmation/', views.donation_confirmation, name='donation_confirmation'),
    path('razorpay-webhook/', views.razorpay_webhook, name='razorpay_webhook'),
]
