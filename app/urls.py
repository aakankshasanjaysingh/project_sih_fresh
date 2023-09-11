
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.create_request, name='create_request'),
]
