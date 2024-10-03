from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donation_amount', 'other_amount', 'citizenship', 'full_name', 'email', 'birth_date', 'pan_number', 'mobile']

        widgets = {
            'donation_amount': forms.RadioSelect(),
            'citizenship': forms.RadioSelect(),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'pan_number': forms.TextInput(attrs={'maxlength': '10', 'placeholder': 'PAN Card No.'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        donation_amount = cleaned_data.get("donation_amount")
        other_amount = cleaned_data.get("other_amount")

        if donation_amount == 'other' and not other_amount:
            self.add_error('other_amount', 'Please specify the other donation amount.')
        return cleaned_data
