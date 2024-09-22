from django.shortcuts import render, get_object_or_404, redirect
from .models import Ministry, VolunteerApplication
from .forms import VolunteerApplicationForm
from django.contrib import messages
from django.views.decorators.cache import never_cache


@never_cache
def ministry_detail(request, url):
    ministry = get_object_or_404(Ministry, url=url)

    if request.method == 'POST':
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            volunteer_application = form.save(commit=False)
            volunteer_application.ministry = ministry
            volunteer_application.save()
            messages.success(request, "Application submitted successfully!")  # Use Django messages framework
            return redirect('ministry_detail', url=ministry.url)  # Redirect to avoid form resubmission
    else:
        form = VolunteerApplicationForm()

    return render(request, 'volunteers/ministry_detail.html', {
        'ministry': ministry,
        'form': form,
    })
