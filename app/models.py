# app/models.py
from django.db import models

class Request(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    pdf = models.FileField(upload_to='pdfs/')  # PDF file upload
    agency_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app'  # Replace 'app' with the actual name of your app



