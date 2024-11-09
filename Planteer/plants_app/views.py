from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
from .models import Plants

# Create your views here.
def all_plants_view(request:HttpRequest):
    plants = Plants.objects.all()
    return render(request, 'plants/all_plants.html', {'plants': plants})

def plants_detail_view(request:HttpRequest, plant_id:int):
    
    plant= Plants.objects.get(pk=plant_id)
    return render(request, 'plants/plants_detail.html', {"plant":plant})


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
        new_plant.save()
        return redirect('main_app:home_view') 
    return render(request, 'plants/new_plants.html')  


def update_plants_view(request:HttpRequest, plant_id=int):
    plant= Plants.objects.get(pk=plant_id)

    if request.method=="Post":
        plant.name=request.POST["name"]
        plant.used_for=request.POST["used_for"]
        plant.category=request.POST["category"]
        plant.is_edible=request.POST["is_edible"]
        if"image" in request.FILES:plant.image= request.FILES["image"]
        plant.save()

        return redirect("plants_app:plants_detail_view", plant_id=plant.id)
    return render(request, 'plants/update_plants.html', {"plant":plant} )


def delete_plants_view(request:HttpRequest, plant_id=int):

    plant= Plants.objects.get(pk=plant_id)
    plant.delete()

    return redirect("main_app:home_view", plant_id=plant.id)


def search_plants_view(request:HttpRequest):
    search_query = request.GET.get('search_query')
    if search_query:
        plants = Plants.objects.filter(name__contains=search_query)
    else:
        plants = None

    context = {
        'plants': plants,
        'search_query': search_query
    }
    return render(request, 'plants/search_plants.html', context)



