from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
from .models import Plants

# Create your views here.
def all_plants_view(request:HttpRequest):
    plants = Plants.objects.all()
    return render(request, 'plants/all_plants.html', {'plants': plants})

def plants_detail_view(request:HttpRequest):
    return render(request, 'plants/plants_detail.html')

def new_plants_view(request:HttpRequest):
    if request.method == "POST":
        name = request.POST['name']
        about = request.POST['about']
        used_for = request.POST['used_for']
        image = request.FILES['image']
        category = request.POST['category']
        is_edible = request.POST.get('is_edible') == 'on'

        new_plant = Plants.objects.create(
            name=name,
            about=about,
            used_for=used_for,
            image=image,
            category=category,
            is_edible=is_edible
        )
        return redirect('main_app:home_view') 
    return render(request, 'plants/new_plants.html')  


def update_plants_view(request:HttpRequest):
    return render(request, 'plants/update_plants.html')

def delete_plants_view(request:HttpRequest):
    return render(request, 'plants/delete_plants.html')

def search_plants_view(request:HttpRequest):
    return render(request, 'plants/search_plants.html')



