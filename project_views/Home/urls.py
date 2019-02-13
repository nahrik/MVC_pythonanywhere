from django.urls import path
from . import views 

urlspatterns = [
    path(' ',views.Home, nama = 'content_home'),
]