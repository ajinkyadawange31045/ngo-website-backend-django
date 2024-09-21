from django.contrib import admin
from .models import Initiative, DriveImage

# Inline configuration for DriveImage
class DriveImageInline(admin.TabularInline):
    model = DriveImage
    extra = 1  # Number of empty forms to display

# Customizing the Initiative admin interface
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'date_of_initiative', 'status', 'url')
    search_fields = ('name', 'title', 'content', 'point_wise')
    list_filter = ('date_of_initiative', 'status')
    prepopulated_fields = {'url': ('name',)}
    
    # Allow editing these fields directly from the list view
    list_editable = ('status',)

    # Fieldsets to organize fields in the admin form
    fieldsets = (
        (None, {
            'fields': ('name', 'title', 'content', 'url', 'status', 'point_wise', 'date_of_initiative')
        }),
        ('Media', {
            'fields': ('image1', 'caption_for_image'),
            'description': 'Upload images or add links in the Drive Images section below.'
        }),
        ('SEO & Tags', {
            'fields': ('tags_for_seo_and_search_bar_in_website',)
        }),
    )

    inlines = [DriveImageInline]

# Register the Initiative model with the customized admin interface
admin.site.register(Initiative, InitiativeAdmin)

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
