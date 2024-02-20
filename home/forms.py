from django import forms
from profiles.models import NewsletterSubscription


# Must create two separate forms as they are rendered on the same page (index)
# W3C was throwing a Duplicate ID error and this seemed to be the only way
class NewsletterSubscriptionForm(forms.ModelForm):
    """
    Newsletter form class for index
    """
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'autocomplete': 'email'
            })
        self.fields['email'].label = ''  # Set the label to an empty string


class NewsletterSubscriptionModalForm(forms.ModelForm):
    """
    Newsletter form class for modal
    """
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'autocomplete': 'email'
            })
        self.fields['email'].label = ''  # Set the label to an empty string
