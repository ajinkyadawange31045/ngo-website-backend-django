from django.shortcuts import render, get_object_or_404, redirect
from .models import Ministry
from django.contrib import messages
from django.views.decorators.cache import never_cache

@never_cache
def ministry_detail(request, url):
    ministry = get_object_or_404(Ministry, url=url)
    # Fetch all ministries except the current one for navigation
    other_ministries = Ministry.objects.exclude(id=ministry.id)[:5]  # Limit to 5 for example

    form_embed = ministry.get_form_embed()

    return render(request, 'volunteers/volunteers_detail.html', {
        'ministry': ministry,
        'form_embed': form_embed,
        'other_ministries': other_ministries,  # Pass the list of other ministries to the template
    })
 
 

def ministry_list(request):
    ministries = Ministry.objects.all()  # Fetch all ministries
    return render(request, 'volunteers/all_volunteers.html', {'ministries': ministries})
