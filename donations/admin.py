from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'donation_amount', 'other_amount', 'citizenship', 'created_at')
    search_fields = ('full_name', 'email', 'mobile')
    list_filter = ('citizenship', 'created_at')
