from django import forms
from .models import Tag

class EditorForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    img_link = forms.URLField(required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
    twitter = forms.CharField()
    meta = forms.CharField()
    instagram = forms.CharField()
    linkedin = forms.CharField()
    choices = []
    for tag in Tag.objects.all():
        choices.append((tag.socialtag_id, tag.name))
    tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices, required=True)