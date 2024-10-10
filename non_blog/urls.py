from django.contrib import admin
from django.urls import path,include
# from gallery.views import home, details, addlike
from .views import *
urlpatterns = [
    path('about-us/',about_us,name="aboutus" ),
    path('advisory-board/',advisory_board,name="leading_team" ),
    path('leadership-team', leadership ,name="leading_team" ),
    path('board-of-trustees/', trustees ,name="trustees" ),
    path('vision-and-mission/', vision_and_mission ,name="vision_and_mission" ),
    path('colleges-covered/', colleges_covered ,name="colleges_covered" ),
    path('educational-seminars/', educational_seminars ,name="educational_seminars" ),
    path('our-experience/', experience ,name="experience" ),
    path('free-education/', free_education ,name="free_education" ),
    path('our-work/', our_work ,name="our_work" ),
    path('our-reach/', our_reach ,name="our_reach" ),
    path('school-covered/', school_covered ,name="school_covered" ),
    path('research/', research ,name="research" ),
    path('donate/', donation ,name="donation" ),
    # path('//',  ,name="" ),
]

from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


