__author__ = 'roopam'

from django import forms

class ImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()