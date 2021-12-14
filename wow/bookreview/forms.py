from django import forms
from .models import Tag

class EditorForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    img_link = forms.URLField(required=True)
    review = forms.CharField(widget=forms.Textarea, required=True)
    twitter = forms.CharField(widget=forms.CharField,)
    meta = forms.CharField(widget=forms.CharField,)
    instagram = forms.CharField(widget=forms.CharField,)
    linkedin = forms.CharField(widget=forms.CharField,)
    