# your_app/admin.py
from django.contrib import admin
from .models import DonationItem

@admin.register(DonationItem)
class DonationItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)

# Optionally, you can customize the admin interface further:
# class DonationItemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'description', 'created_at')
#     search_fields = ('name',)
#     list_filter = ('created_at',)
