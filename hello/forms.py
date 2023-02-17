from django import forms
from .models import Post, Upload


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text',)


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ["file"]
