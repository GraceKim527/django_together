from django import forms
from .models import KangBlog, KangComment

class CreateForm(forms.ModelForm):
    class Meta:
        model = KangBlog
        fields = ['title', 'content']#, 'image'

class CommentForm(forms.ModelForm):
    class Meta:
        model = KangComment
        fields = ['text']