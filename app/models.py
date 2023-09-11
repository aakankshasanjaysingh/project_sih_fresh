# app/models.py
from django.db import models
import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
        ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
        valid_extensions = ['.pdf','.jpg', '.png',]
        if not ext.lower() in valid_extensions:
            raise ValidationError('Unsupported file extension.')
class Request(models.Model):

    class Meta:
        app_label = 'app'  # Replace 'app' with the actual name of your app

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    video_name = models.CharField(max_length=200,null=True,blank=True)
    pdf = models.FileField(upload_to='pdfs/',validators=[validate_file_extension])  # PDF file upload
    agency_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title




