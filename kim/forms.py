from django import forms
from .models import Gram, Gram_Comment
class CreateForm(forms.ModelForm):
    class Meta:
        model = Gram
        fields = ['title', 'writer', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Gram_Comment
        fields = ['text'] 