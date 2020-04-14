from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    """Form for post model"""
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')
        

