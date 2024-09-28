from django.urls import path
from . import views

app_name = 'initiatives'

urlpatterns = [
    path('initiatives/', views.initiative_page, name='initiative_page'),  # All initiatives page
    path('initiatives/<slug:url>', views.initiative_detail, name='initiative_detail'),  # Detail view for a specific initiative
]
