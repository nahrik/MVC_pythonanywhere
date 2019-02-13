from django.urls import path
from . import views 

urlspatterns = [
    path(' ',views.Mentee, nama = 'nama_mentee'),
]