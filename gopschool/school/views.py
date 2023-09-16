from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request): #Function หน้าแรกให้ทำอะไร
	return HttpResponse('<h1>Hello My Website.</h1>')