from django.urls import path
from . import views

app_name = 'stories_detail'

urlpatterns = [
    # path('', views.initiative_list, name='initiative_list'),  # List all Stories_detail
    path('impact-stories/<slug:url>', views.stories_detail, name='stories_detail'),  # Detail view for a specific initiative
]
