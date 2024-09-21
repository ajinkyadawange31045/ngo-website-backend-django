from django.shortcuts import render, get_object_or_404
from .models import Stories,DriveImage




def stories_detail(request, url):
    # Fetch specific initiative
    stories = get_object_or_404(Stories, url=url)
    drive_images = DriveImage.objects.all()
    # Render to the detail template
    return render(request, 'impact_stories/stories.html', {'stories': stories,'drive_images':drive_images,})
