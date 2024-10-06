from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):  # Form class name should be specific
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your full name',
            'required': 'required'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email address',
            'required': 'required'
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Subject of your message',
            'required': 'required'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Write your message here',
            'required': 'required'
        })
