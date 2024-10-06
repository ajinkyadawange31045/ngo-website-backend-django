from django.urls import path
from .views import ministry_detail,ministry_list

urlpatterns = [
    path('volunteer-for-/<slug:url>/', ministry_detail, name='volunteer_detail'),
    path('volunteering-options/', ministry_list, name='ministry_list'), 
]
