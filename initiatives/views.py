from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Initiative, DriveImage

def initiative_detail(request, url):
    # Fetch specific initiative
    initiative = get_object_or_404(Initiative, url=url)
    drive_images = DriveImage.objects.all()
    # Render to the detail template
    return render(request, 'initiatives/initiative_detail.html', {'initiative': initiative, 'drive_images': drive_images})

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Initiative

def initiative_page(request):
    # Order initiatives by the date field in descending order
    i1 = Initiative.objects.all().order_by('-date_of_initiative')  # Use the relevant field for sorting

    # Set up pagination
    paginator = Paginator(i1, 15)  # Show 15 initiatives per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    initiatives_page = paginator.get_page(page_number)  # Get the initiatives for the current page

    context = {
        'initiatives_page': initiatives_page,
    }
    return render(request, 'initiatives/all_initiatives.html', context)

