from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Contact
from plants_app.models import Plants



# Create your views here.

def home_view(request:HttpRequest):
    plants = Plants.objects.all().order_by('-created_at') 
    return render(request, 'main/home.html', {'plants': plants})

def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )
        contact.save()
        return redirect('main_app:messages_view')
    return render(request, 'main/contact.html')

def messages_view(request):
    messages = Contact.objects.all()
    return render(request, 'main/messages.html', {'messages': messages})









