from datetime import datetime
from django import forms
from django.forms.widgets import  CheckboxSelectMultiple
from .models import *


class EditorForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    img_link = forms.URLField(required=False)
    review = forms.CharField(widget=forms.Textarea, required=True)
    instagram = forms.CharField(widget=forms.TextInput,required=False)
    meta = forms.CharField(widget=forms.TextInput,required=False)
    linkedin = forms.CharField(widget=forms.TextInput,required=False)
    twitter = forms.CharField(widget=forms.TextInput,required=False)
    date_created =datetime.now()
    social = []
    for tag in Tag.objects.all():
        social.append((tag.socialtag_id, tag.name))
    social = forms.MultipleChoiceField(widget=CheckboxSelectMultiple, choices=social, required=False)