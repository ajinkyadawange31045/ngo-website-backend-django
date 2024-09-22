from django.db import models
from ckeditor.fields import RichTextField
class Ministry(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ministries/')
    caption = models.TextField(blank=True)
    url = models.CharField(max_length=100)
    youtube_link = models.URLField(blank=True)
    instructions = RichTextField(blank=True,help_text='Detailed instructions or content about the ministry.') 
    tag_for_seo = models.TextField(help_text='Tags for SEO purposes.')

    def __str__(self):
        return self.title

class VolunteerApplication(models.Model):
    ministry = models.ForeignKey(Ministry, related_name='applications', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.role}"
