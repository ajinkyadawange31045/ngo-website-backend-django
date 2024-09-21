from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
 

class Initiative(models.Model):
    initiative_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=45, blank=True)
    excert = models.CharField(max_length=200,blank=True)
    point_wise = RichTextField(blank=True)
    content = RichTextField(blank=True)
    url = models.CharField(max_length=100, unique=True)
    image1 = models.ImageField(upload_to='initiatives/', blank=True)
    caption_for_image = models.CharField(max_length=100, blank=True)
    date_of_initiative = models.DateTimeField(default=timezone.now)
    tags_for_seo_and_search_bar_in_website = models.TextField(
        help_text='Add tags for search and SEO purposes.'
    )
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('initiatives:initiative_detail', args=[str(self.pk)]) 


class DriveImage(models.Model):
    title = models.CharField(max_length=50)
    image_link = models.URLField()  # Store the original Google Drive link
    initiative = models.ForeignKey(Initiative, related_name='drive_images', on_delete=models.CASCADE)

    @property
    def embed_link(self):
        # Convert the original link to an embed link
        return self.image_link.replace('/view?usp=sharing', '/preview')

    def __str__(self):
        return self.title
