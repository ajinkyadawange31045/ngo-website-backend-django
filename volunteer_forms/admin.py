from django.contrib import admin
from .models import Ministry

@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'youtube_link')
    search_fields = ('title', 'instructions')
