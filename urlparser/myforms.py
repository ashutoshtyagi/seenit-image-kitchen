__author__ = 'roopam'

from django import forms

class SubmitForm(forms.Form):
    url = forms.URLField(label='Url', max_length=100)
