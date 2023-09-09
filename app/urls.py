
from django.urls import path
from . import views

urlpatterns = [
    path('create_request/', views.create_request, name='create_request'),
]
