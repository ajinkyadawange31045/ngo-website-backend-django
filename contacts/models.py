from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically adds timestamp

    def __str__(self):
        return f"{self.name} - {self.subject}"
