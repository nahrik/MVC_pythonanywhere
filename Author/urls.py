from django.urls import path
from . import views 

urlspatterns = [
    path(' ',views.Author, nama = 'nama_author'),
]