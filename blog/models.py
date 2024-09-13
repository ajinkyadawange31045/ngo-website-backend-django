from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# from django.utils.html import HTMLField
# from tinymce import models as tinymce_models
from django.utils.html import format_html
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
# Create your models here.

from django.db import models

class CustomAutoPrimaryKeyField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['primary_key'] = True
        kwargs['editable'] = True  # Set editable to True
        super().__init__(*args, **kwargs)

    def get_pk_value_on_save(self, instance):
        if instance._state.adding:
            max_id = instance.__class__.objects.aggregate(models.Max('id'))['id__max']
            if max_id is not None:
                return max_id + 1
            else:
                return 1
        else:
            return super().get_pk_value_on_save(instance)


# catergories of post
class Category(models.Model):
    # cat_id = models.AutoField(primary_key=True)
    cat_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    url = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))
    def __str__(self):
        return self.title

# post with image for publishing
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    blog_views =models.IntegerField(default=0,editable=False)
    main_long_title = models.CharField(max_length=250)
    excerpt = models.TextField(max_length=1000)
    thumbnail  = models.ImageField(upload_to='post_thumbnail/')
    thumbnail_caption = models.CharField(max_length=100, default='Image related to blog')
    url = models.CharField(max_length=100,unique=True)
    publish = models.DateTimeField(default=timezone.now)
    content_before_image = RichTextField(blank=True)
    image_for_post = models.ImageField(upload_to='image_for_post/', blank=True)
    caption_for_image = models.CharField(max_length=100, blank=True)
    content_after_image = RichTextField(blank=True)
    quote_related_to_post = models.TextField(blank=True)
    author_of_quote = models.CharField(max_length=50,blank=True)
    tags_for_seo_and_search_bar_in_website = models.TextField(help_text='Add tags(this tags will be for search bar of the webstie as well as for SEO stuffs, so be particular while adding, do research for the keywords, and add properly.')
    # favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    # likes = models.ManyToManyField(
    #     User, related_name='like', default=None, blank=True)
    # like_count = models.BigIntegerField(default='0')
    # objects = models.Manager()  # default manager
    # newmanager = NewManager()  # custom manager
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
    @property
    def get_comments(self):
        return self.comment_content.all()

