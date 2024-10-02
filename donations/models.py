# your_app/models.py
from django.db import models

class DonationItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    # Optionally add an image field
    # image = models.ImageField(upload_to='donation_items/', null=True, blank=True)

    def __str__(self):
        return self.name



class Cart(models.Model):
    items = models.ManyToManyField(DonationItem, through='CartItem')

    def total_price(self):
        return sum(item.item_total() for item in self.cartitem_set.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    donation_item = models.ForeignKey(DonationItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def item_total(self):
        return self.donation_item.price * self.quantity
