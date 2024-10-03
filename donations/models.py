# models.py
from django.db import models

class Donation(models.Model):
    AMOUNT_CHOICES = [
        (4500, '₹ 4500'),
        (9000, '₹ 9000'),
        (13500, '₹ 13,500'),
        (18000, '₹ 18,000'),
    ]

    CITIZENSHIP_CHOICES = [
        ('indian', 'Indian Citizen'),
        ('nri', 'Indian Citizen (NRI)'),
        ('foreign', 'Foreign National'),
    ]

    donation_amount = models.DecimalField(max_digits=10, decimal_places=2, choices=AMOUNT_CHOICES, verbose_name="Donation Amount")
    other_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Other Amount")
    citizenship = models.CharField(max_length=20, choices=CITIZENSHIP_CHOICES, verbose_name="Citizenship")
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField(blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="PAN Number")
    mobile = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    # Razorpay fields
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Donation by {self.full_name} - ₹{self.donation_amount or self.other_amount}"
