# admin.py
from django.contrib import admin
from .models import FundraisingCampaign, Donation

class FundraisingCampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'raised_amount', 'goal_amount', 'progress')
    search_fields = ('title',)
    list_filter = ('progress',)

class DonationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'campaign', 'amount_donated', 'created_at')
    search_fields = ('full_name', 'email_id', 'campaign__title')  # Search by campaign title
    list_filter = ('campaign', 'created_at')

# Register your models here
admin.site.register(FundraisingCampaign, FundraisingCampaignAdmin)
admin.site.register(Donation, DonationAdmin)
