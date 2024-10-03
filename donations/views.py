# views.py
import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import DonationForm
from .models import Donation

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            # Save donation details locally
            donation = form.save(commit=False)

            # Razorpay client instance
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            # Create Razorpay order
            order_amount = int(donation.donation_amount * 100)  # Amount in paise
            order_currency = 'INR'
            order_receipt = f'donation_rcptid_{donation.id}'
            razorpay_order = client.order.create({
                'amount': order_amount,
                'currency': order_currency,
                'receipt': order_receipt,
                'payment_capture': '1'
            })

            # Save Razorpay order details
            donation.razorpay_order_id = razorpay_order['id']
            donation.save()

            # Redirect to payment page
            context = {
                'order_id': razorpay_order['id'],
                'razorpay_key': settings.RAZORPAY_KEY_ID,
                'amount': order_amount,
                'donation': donation
            }
            return render(request, 'donations/razorpay_payment.html', context)

    else:
        form = DonationForm()

    return render(request, 'donations/donate.html', {'form': form})


def donation_confirmation(request):
    return render(request, 'donations/donation_confirmation.html')

# views.py (add a new view for webhook)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import razorpay

@csrf_exempt
def razorpay_webhook(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    try:
        payload = request.body
        signature = request.headers.get('X-Razorpay-Signature')

        # Razorpay utility to verify signature
        client.utility.verify_payment_signature({
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': signature
        })

        # Save the transaction details in Donation model
        donation = Donation.objects.get(razorpay_order_id=request.POST.get('razorpay_order_id'))
        donation.razorpay_payment_id = request.POST.get('razorpay_payment_id')
        donation.razorpay_signature = signature
        donation.save()

        return redirect('donation_confirmation')

    except razorpay.errors.SignatureVerificationError as e:
        return HttpResponseBadRequest()
