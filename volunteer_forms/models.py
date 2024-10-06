from django.db import models
from ckeditor.fields import RichTextField
import re
class Ministry(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ministries/')
    caption = models.TextField(blank=True)
    url = models.CharField(max_length=100)
    youtube_link = models.URLField(blank=True)
    instructions = RichTextField(blank=True,help_text='Detailed instructions or content about the ministry.') 
    form_embed = models.CharField(blank=True,max_length=500)
    tag_for_seo = models.TextField(help_text='Tags for SEO purposes.')

    def __str__(self):
        return self.title
    
    @property
    def youtube_embed_link(self):
        if self.youtube_link:
            return self.youtube_link.replace("watch?v=", "embed/")
        return None

    def get_form_embed(self):
        if self.form_embed:
            # Use regex to find the height attribute and increase it by 100px
            return re.sub(r'height="(\d+)"', lambda m: f'height="{int(m.group(1)) + 100}"', self.form_embed)
        return None