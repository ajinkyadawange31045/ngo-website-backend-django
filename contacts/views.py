from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.contrib import messages
from django.views.decorators.cache import never_cache

@never_cache
def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form directly
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact_us')  # Prevent resubmission
    else:
        form = ContactUsForm()

    return render(request, 'base/contact_us.html', {
        'form': form,
    })
