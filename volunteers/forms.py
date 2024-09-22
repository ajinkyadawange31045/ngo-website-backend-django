from django import forms
from .models import VolunteerApplication

class VolunteerApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ['name', 'email', 'role', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
        self.fields['role'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'rows': 3, 'required': 'required'})
