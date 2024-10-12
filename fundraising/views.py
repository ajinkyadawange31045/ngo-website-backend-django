from django.shortcuts import render, get_object_or_404, redirect
from .models import FundraisingCampaign, Donation
from .forms import DonationForm
import razorpay
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Initialize Razorpay client with test credentials
razorpay_client = razorpay.Client(auth=("rzp_test_9hLh9fBj8OYOYg", "S0Q6ZQpeRgf0XnHThJXOcFmo"))

def donation_page(request, campaign_id):
    campaign = get_object_or_404(FundraisingCampaign, id=campaign_id)

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            # Check the arithmetic verification
            if form.cleaned_data['arithmetic_verification'] != 6:
                form.add_error('arithmetic_verification', 'Incorrect answer. Please try again.')
                return render(request, 'fundraising/donations.html', {'campaign': campaign, 'form': form})

            # Process the donation...
            
            # Clear the form data by resetting it
            form = DonationForm()  # Reset form after successful submission

            # Redirect to the Razorpay payment page
            return render(request, 'fundraising/payment.html', {
                'order_id': order_id,
                'amount': amount,
                'campaign_title': campaign.title,
            })
    else:
        form = DonationForm()

    return render(request, 'fundraising/donations.html', {'campaign': campaign, 'form': form})


@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        payment_id = data.get('razorpay_payment_id')
        order_id = data.get('razorpay_order_id')

        # Fetch donation data from the session
        donation_data = request.session.get('donation_data', None)
        if donation_data:
            donation_id = donation_data['donation_id']
            amount = donation_data['amount']
            campaign_id = donation_data['campaign_id']

            # Save the donation to the database
            donation = Donation.objects.get(id=donation_id)
            donation.payment_id = payment_id  # Store the Razorpay payment ID
            donation.donation_status = "Paid"  # Set status to Paid
            donation.save()  # Update donation with payment ID and status

            # Clear session data
            del request.session['donation_data']
            return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'failed'})
