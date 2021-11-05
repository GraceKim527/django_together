from django import forms
from .models import S_Blog, Song_comment, Song_hashtag

class CreateForm(forms.ModelForm):
    class Meta:
        model = S_Blog
        fields = ['title', 'writer', 'content', 'image', 'hashtags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Song_comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Song_hashtag
        fields = ['name']