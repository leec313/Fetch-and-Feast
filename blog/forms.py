from .models import (
    Post,
    Comment
)
from tinymce.widgets import TinyMCE
from django import forms


class PostForm(forms.ModelForm):
    """
    Form class for creating a blog post
    """
    content = forms.CharField(widget=TinyMCE(attrs={
        'cols': 80, 'rows': 30, 'class': 'tinymce'}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'excerpt']


class CommentForm(forms.ModelForm):
    """
    Form class for posting a comment
    """
    body = forms.CharField(widget=forms.Textarea(
            attrs={'placeholder': 'Your comment here'}), label=False)

    class Meta:
        model = Comment
        fields = ('body',)
