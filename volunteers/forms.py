from django import forms
from .models import VolunteerApplication

class VolunteerApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ['name', 'email', 'role', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
            'placeholder': 'Enter your full name'  # Add placeholder
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
            'placeholder': 'Enter your email address'  # Add placeholder
        })
        self.fields['role'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
            'placeholder': 'Specify your role or volunteer title'  # Add placeholder
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'rows': 3,
            'required': 'required',
            'placeholder': 'Write your message or suggestion'  # Add placeholder
        })
