from django.contrib import admin
from .models import Stories, DriveImage

class DriveImageInline(admin.TabularInline):
    model = DriveImage
    extra = 1

class StoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status', 'url')
    search_fields = ('title', 'content')
    list_filter = ('date', 'status')
    prepopulated_fields = {'url': ('title',)}
    list_editable = ('status',)
    
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'url', 'status', 'excert', 'youtube_video')
        }),
        ('Media', {
            'fields': ('image1', 'caption_for_image')
        }),
        ('SEO & Tags', {
            'fields': ('tags_for_seo_and_search_bar_in_website',)
        }),
        ('Important Dates', {
            'fields': ('date',)
        }),
    )
    
    inlines = [DriveImageInline]

admin.site.register(Stories, StoriesAdmin)

# Register the DriveImage model to view it as a separate table in the admin
@admin.register(DriveImage)
class DriveImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_link', 'initiative')
    search_fields = ('title', 'image_link')
    list_filter = ('initiative',)
    
    # Allow editing of all fields in the DriveImage model
    fieldsets = (
        (None, {
            'fields': ('title', 'image_link', 'initiative')
        }),
    )
