# akasih/forms.py
from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'agency_name', 'description', 'pdf']
