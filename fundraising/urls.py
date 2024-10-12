# urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path('donate/<int:campaign_id>/', views.donation_page, name='donation_page'), 
    # path('donate/<int:campaign_id>/', donation_page, name='donation_page'),
    path('payment/success/', views.payment_success, name='payment_success'),
]
