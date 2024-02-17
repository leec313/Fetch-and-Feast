from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Rating


class ProductForm(forms.ModelForm):
    """
    Form for adding/updating products
    """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class CategoryForm(forms.ModelForm):
    """
    Form for adding a category
    """
    class Meta:
        model = Category
        fields = ['friendly_name']
        labels = {
            'friendly_name': '',
        }


class RatingForm(forms.ModelForm):
    """
    For for ratings on products
    """
    # Define choices for the rating
    SCORE_CHOICES = [(str(i), str(i)) for i in range(1, 6)]

    # Update the score field to use the ChoiceField
    score = forms.ChoiceField(
        choices=SCORE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'star-radio'}),
        label='',  # Set the label to an empty string
        required=False,
    )

    class Meta:
        model = Rating
        fields = ['title', 'body', 'score']

        labels = {
            'title': 'Rating Title',
            'body': 'Tell us what you think!',
        }
