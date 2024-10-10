# admin.py

from django.contrib import admin
from .models import Trustees, Leading_Team, Advisory

@admin.register(Trustees)
class TrusteesAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'about')  # Customize fields to display in list view
    search_fields = ('name', 'designation')  # Enable search functionality

@admin.register(Leading_Team)
class LeadingTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'work', 'area', 'about')
    search_fields = ('name', 'work', 'area')

@admin.register(Advisory)
class AdvisoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'work', 'about')
    search_fields = ('name', 'work')
