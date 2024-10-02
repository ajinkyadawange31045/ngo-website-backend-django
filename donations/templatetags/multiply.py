# your_app/templatetags/multiply.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def get_item(cart, item_id):
    return cart.get(str(item_id), 0)  # Return quantity or 0 if item_id not in cart
