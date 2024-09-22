from django.shortcuts import render, get_object_or_404
from .models import Initiative,DriveImage




def initiative_detail(request, url):
    # Fetch specific initiative
    initiative = get_object_or_404(Initiative, url=url)
    drive_images = DriveImage.objects.all()
    # Render to the detail template
    return render(request, 'initiatives/initiative_detail.html', {'initiative': initiative,'drive_images':drive_images,})

def initiative_page(request):
    i1 = Initiative.objects.all()
    context = {
        'i1': i1,
    }
    return render(request, 'initiatives/all_initiatives.html', context)