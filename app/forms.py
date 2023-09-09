# akasih/forms.py
from django import forms

class RequestForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':40}))
    pdf = forms.FileField()
    agency_name = forms.CharField(max_length=100)
    
