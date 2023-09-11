# akasih/forms.py
from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'agency_name', 'description', 'pdf','video_name']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control','placeholder':"Your Name"}),
        'agency_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Agency Name'}),
        'pdf':forms.FileInput(attrs={'class':'form-control'}),
        'video_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Your Video Name'}),
        'description': forms.Textarea(attrs={'class':'form-control','rows':8,'cols':4,'placeholder':'Describe your video'})
        }
        
        labels = {
            'title': 'Name of the user',
            'agency_name': 'Agency or Organization Name',
            'pdf': 'Upload your ppt or pdf in jpg,pdf,png format.',
            'video_name': 'Name of the video',
            'description': 'Describe your video',
        }
        