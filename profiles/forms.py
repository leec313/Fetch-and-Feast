from django import forms
from .models import UserProfile

from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'default_phone_number', 'default_street_address1',
                  'default_street_address2', 'default_town_or_city', 'default_county',
                  'default_postcode', 'default_country']

    user_username = forms.CharField(max_length=150, label='Username')
    user_email = forms.EmailField(label='Email')
    user_first_name = forms.CharField(max_length=30, label='First Name')
    user_last_name = forms.CharField(max_length=30, label='Last Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_username': 'Username',
            'user_email': 'Email',
            'user_first_name': 'First Name',
            'user_last_name': 'Last Name',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County/State',
        }

        for field in self.fields:
            if field in placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
                self.fields[field].label = False