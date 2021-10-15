from django import forms
from .models import S_Blog, Song_comment

class CreateForm(forms.ModelForm):
    class Meta:
        model = S_Blog
        fields = ['title', 'writer', 'content', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Song_comment
        fields = ['text']