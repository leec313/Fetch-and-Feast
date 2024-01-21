from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.models import EmailAddress
from .widgets import CustomClearableFileInput
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_image',
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_county',
            'default_postcode',
            'default_country',
                ]

    user_username = forms.CharField(max_length=150, label='Username')
    user_email = forms.EmailField(label='Email')
    user_first_name = forms.CharField(max_length=30, label='First Name')
    user_last_name = forms.CharField(max_length=30, label='Last Name')
    profile_image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set initial values for custom fields based on the profile instance
        if self.instance:
            self.fields['user_username'].initial = self.instance.user.username
            self.fields['user_email'].initial = self.instance.user.email
            self.fields['user_first_name'].initial = self.instance.user.first_name
            self.fields['user_last_name'].initial = self.instance.user.last_name

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


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, **kwargs):
    """
    Update the user profile when the User is saved
    """
    try:
        profile = instance.userprofile
        profile.user_username = instance.username
        profile.user_email = instance.email
        profile.user_first_name = instance.first_name
        profile.user_last_name = instance.last_name
        profile.save()
    except UserProfile.DoesNotExist:
        pass


@receiver(post_save, sender=User)
def update_user_email_addresses(sender, instance, **kwargs):
    """
    Update the user's email addresses when the User is saved
    """
    try:
        email_addresses = EmailAddress.objects.filter(user=instance)
        for email_address in email_addresses:
            email_address.email = instance.email
            email_address.save()
    except EmailAddress.DoesNotExist:
        pass