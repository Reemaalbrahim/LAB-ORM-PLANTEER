from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Contact
from plants_app.models import Plants



# Create your views here.

def home_view(request:HttpRequest):
    plants = Plants.objects.all().order_by('-created_at') 
    return render(request, 'main/home.html', {'plants': plants})

def contact_view(request:HttpRequest):
    return render(request, 'main/contact.html')

def messages_view(request:HttpRequest):
    return render(request, 'main/messages.html')

