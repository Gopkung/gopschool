from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request): #Function หน้าแรกให้ทำอะไร
	#return HttpResponse('<h1>Hello My Website.</h1>') #ให้แสดงค่าที่หน้าเว็บ
	return render(request, 'school/home.html') #ให้เรียกไฟล์ home.html

def AboutPage(request):
	return render(request, 'school/about.html') #ให้เรียกไฟล์ about.html