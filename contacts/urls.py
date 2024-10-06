from django.urls import path
from .views import contact

urlpatterns = [
    path('contact-us/', contact, name='contact_us'),
]
