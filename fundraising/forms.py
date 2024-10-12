from django import forms

class DonationForm(forms.Form):
    FULL_NAME_CHOICES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Dr', 'Dr'),
        ('Other', 'Other'),
    ]

    full_name_prefix = forms.ChoiceField(
        choices=FULL_NAME_CHOICES,
        label="Prefix",
        required=True
    )
    full_name = forms.CharField(
        max_length=100,
        label="Full Name*",
        required=True
    )
    email_id = forms.EmailField(
        label="Email ID*",
        required=True
    )
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Birthdate",
        required=True
    )
    pan_number = forms.CharField(
        max_length=10,
        label="PAN Number*",
        required=True
    )
    mobile_no = forms.CharField(
        max_length=15,
        label="Mobile No.*",
        required=True
    )
    alternate_mobile_no = forms.CharField(
        max_length=15,
        label="Alternate Mobile No.",
        required=False
    )
    whatsapp_number = forms.CharField(
        max_length=15,
        label="WhatsApp Number",
        required=False
    )
    pin_code = forms.CharField(
        max_length=6,
        label="Pin Code*",
        required=True
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        label="Address*",
        required=True
    )
    preference_state = forms.ChoiceField(
        choices=[
            ('', 'Select your Preference State'),
            ('state1', 'State 1'),
            ('state2', 'State 2'),
            # Add other states as needed
        ],
        label="Preference State*",
        required=True
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Donation Amount*",
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter amount in INR'})
    )

    # Arithmetic verification
    arithmetic_verification = forms.IntegerField(
        label="Please solve: 3 + 3 = ?",
        required=True
    )

    privacy_policy = forms.BooleanField(
        label="I have read through the website's Privacy Policy & Terms and Conditions to make a donation.",
        required=True
    )
