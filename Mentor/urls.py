from django.urls import path
from . import views 

urlspatterns = [
    path(' ',views.Mentor, nama = 'nama_mentor'),
]