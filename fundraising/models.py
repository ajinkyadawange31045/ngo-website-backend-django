# models.py
from django.db import models

class FundraisingCampaign(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='fundraising_images/')
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    progress = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage progress

    def __str__(self):
        return self.title

    def get_progress_percentage(self):
        return (self.raised_amount / self.goal_amount) * 100 if self.goal_amount else 0


class Donation(models.Model):
    campaign = models.ForeignKey(FundraisingCampaign, on_delete=models.CASCADE)
    full_name_prefix = models.CharField(max_length=10)
    full_name = models.CharField(max_length=100)
    email_id = models.EmailField()
    birthdate = models.DateField()
    pan_number = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=15)
    alternate_mobile_no = models.CharField(max_length=15, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6)
    address = models.TextField()
    preference_state = models.CharField(max_length=100)
    amount_donated = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Donation by {self.full_name} for {self.campaign.title}"