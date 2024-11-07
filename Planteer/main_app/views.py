from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Contact


# Create your views here.

def home_view(request:HttpRequest):
    return render(request, 'main/home.html')

def contact_view(request:HttpRequest):
    return render(request, 'main/contact.html')

def messages_view(request:HttpRequest):
    return render(request, 'main/messages.html')






