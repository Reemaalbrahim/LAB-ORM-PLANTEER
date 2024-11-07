from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
from .models import Plants

# Create your views here.
def all_plants_view(request:HttpRequest):
    return render(request, 'plants/all_plants.html')

def plants_detail_view(request:HttpRequest):
    return render(request, 'plants/plants_detail.html')

def new_plants_view(request:HttpRequest):
    return render(request, 'plants/new_plants.html')

def update_plants_view(request:HttpRequest):
    return render(request, 'plants/update_plants.html')

def delete_plants_view(request:HttpRequest):
    return render(request, 'plants/delete_plants.html')

def search_plants_view(request:HttpRequest):
    return render(request, 'plants/search_plants.html')

