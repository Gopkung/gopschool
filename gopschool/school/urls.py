from django.urls import path
from .views import HomePage, AboutPage #ดึง Function HomePage ในไฟล์ views.py

urlpatterns = [
    path('',HomePage, name = 'home-page'), #กำหนด URL หากไม่ได้ระบุอะไรต่อท้าย ให้ไปเรียก Function HomePage
    path('about/', AboutPage, name = 'about-page') #กำหนด URL หากระบุ about ต่อท้าย ให้ไปเรียก Function AboutPage
]