from django.urls import path
from .views import ministry_detail

urlpatterns = [
    path('volunteer/<slug:url>/', ministry_detail, name='ministry_detail'),
]
