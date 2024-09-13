from django.contrib import admin
from .models import GalleryImage

# Register your models here.

# class GalleryImage_Admin(admin.ModelAdmin):
#     list_display = ('id', 'image', 'get_tags')
#     search_fields = ('tags',)

#     def get_tags(self, obj):
#         return ", ".join([tag.name for tag in obj.tags.all()])
#     get_tags.short_description = 'Tags'

# admin.site.register(GalleryImage, GalleryImage_Admin)
