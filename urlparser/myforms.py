__author__ = 'roopam'

from django import forms
from models import Image

class SubmitForm(forms.Form):
    url = forms.URLField(label='Url', max_length=100)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
