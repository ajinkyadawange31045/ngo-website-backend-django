from django.urls import path
from . import views

app_name = 'initiatives'

urlpatterns = [
    # path('', views.initiative_list, name='initiative_list'),  # List all initiatives
    path('initiatives/<slug:url>', views.initiative_detail, name='initiative_detail'),  # Detail view for a specific initiative
]
