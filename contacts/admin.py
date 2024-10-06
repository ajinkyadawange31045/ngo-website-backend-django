import csv  # Make sure to import the CSV module
from django.http import HttpResponse
from django.contrib import admin
from .models import ContactUs  # Replace with your actual model name

def export_as_csv(modeladmin, request, queryset):
    """
    Export selected items to CSV file.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
    writer = csv.writer(response)

    # Optionally, define headers for the CSV file
    writer.writerow(['name', 'email', 'subject','message','created_at'])  # Adjust this according to your model fields

    # Write the data
    for obj in queryset:
        writer.writerow([obj.name, obj.email, obj.subject, obj.message, obj.created_at])  # Adjust according to your model fields

    return response

export_as_csv.short_description = "Export Selected as CSV"




from django.contrib.admin import SimpleListFilter

class DateRangeFilter(SimpleListFilter):
    title = 'Date Range'
    parameter_name = 'date_range'

    def lookups(self, request, model_admin):
        return (
            ('2024-01-01,2024-01-30', 'January 2024'),
            # Add more ranges as needed
        )

    def queryset(self, request, queryset):
        if self.value():
            start_date, end_date = self.value().split(',')
            queryset = queryset.filter(created_at__range=[start_date, end_date])
        return queryset


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at', 'name')
    actions = [export_as_csv]
    list_filter = (DateRangeFilter, 'created_at')  # Add custom date range filter here