from django import forms
from profiles.models import NewsletterSubscription


class NewsletterSubscriptionForm(forms.ModelForm):
    """
    Newsletter form class
    """
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Additional email validation logic can be added here if needed
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter your email'})
