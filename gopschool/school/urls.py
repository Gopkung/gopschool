from django.urls import path
from .views import HomePage #ดึง Function HomePage ในไฟล์ views.py

urlpatterns = [
    path('',HomePage)
]