# views.py
from django.shortcuts import render, redirect
from .models import DonationItem

def get_cart(request):
    # Retrieve cart from session or create a new one
    if 'cart' not in request.session:
        request.session['cart'] = []
    return request.session['cart']


# your_app/views.py
from django.shortcuts import render, redirect
from .models import DonationItem

# your_app/views.py
from django.shortcuts import render, redirect
from .models import DonationItem

def donation_items(request):
    items = DonationItem.objects.all()
    return render(request, 'donations-cart/donation_items.html', {'items': items})

def view_cart(request):
    # Ensure cart is a dictionary
    cart = request.session.get('cart', {})
    items = DonationItem.objects.filter(id__in=cart.keys())
    total_price = sum(item.price * cart[str(item.id)] for item in items)
    return render(request, 'donations-cart/view_cart.html', {'items': items, 'cart': cart, 'total_price': total_price})

def add_to_cart(request):
    if request.method == 'POST':  # Check if the request method is POST
        item_id = request.POST.get('item_id')  # Get the item ID from the submitted form
        quantity = int(request.POST.get('quantity', 0))  # Get the quantity (default to 0)

        if quantity > 0:  # Only add if quantity is greater than 0
            # Retrieve the cart from the session and ensure it's a dictionary
            cart = request.session.get('cart', {})  
            if not isinstance(cart, dict):  # Ensure cart is a dictionary
                cart = {}
                
            # Update cart with item quantities
            if item_id in cart:
                cart[item_id] += quantity  # Update quantity if item already exists
            else:
                cart[item_id] = quantity  # Add new item to cart

            # Save updated cart back to session
            request.session['cart'] = cart  

    return redirect('donations-cart/donation_items')


def payment_page(request):
    cart = get_cart(request)
    item_ids = [item['id'] for item in cart]
    items = DonationItem.objects.filter(id__in=item_ids)

    total_price = sum(item.price * next(i['quantity'] for i in cart if i['id'] == item.id) for item in items)
    return render(request, 'donations-cart/payment_page.html', {'total_price': total_price})
