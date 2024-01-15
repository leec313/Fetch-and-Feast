from .models import (
    Post,
    Comment
)
from django import forms


class PostForm(forms.ModelForm):
    """
    Form class for creating a blog post
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'excerpt']


class CommentForm(forms.ModelForm):
    """
    Form class for posting a comment
    """
    body = forms.CharField(widget=forms.Textarea(
            attrs={'placeholder': 'Your comment here'}))

    class Meta:
        model = Comment
        fields = ('body',)
