from django.contrib import admin
from .models import Ministry, VolunteerApplication

@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'youtube_link')
    search_fields = ('title', 'instructions')

@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'ministry', 'role', 'email')
    search_fields = ('name', 'email', 'role')
