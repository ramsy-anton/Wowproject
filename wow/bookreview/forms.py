from django import forms


class EditorForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    img_link = forms.URLField(required=False)
    review = forms.CharField(widget=forms.Textarea, required=True)
    twitter = forms.CharField(max_length=1000,required=False)
    meta = forms.CharField(max_length=1000,required=False)
    instagram = forms.CharField(max_length=1000,required=False)
    linkedin = forms.CharField(max_length=1000,required=False)
    