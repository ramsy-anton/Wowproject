from django import forms
from .models import Tag
class EditorForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    img_link = forms.URLField(required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
    twitter = forms.URLField(Tag,max_length=100)
    meta = forms.URLField(Tag,max_length=100)
    instagram = forms.URLField(Tag,max_length=100)
    linkedin = forms.URLField(Tag,max_length=100)
    choices = []
    for tag in Tag.objects.all():
        choices.append((tag.tag_id, tag.name))
    tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices, required=True)