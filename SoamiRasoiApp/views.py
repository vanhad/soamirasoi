from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Food,Contact
from django.contrib import messages


food = Food.objects.all()
allFood = []

catFood = Food.objects.values('ItemCat','id')
cats = {item['ItemCat'] for item in catFood}


# Create your views here.

def index(request):
    return render(request, 'index.html', {'food': food,'cats': cats})
    # return HttpResponse("hello")

def about(request):
    return render(request, 'about.html')

def contactUs(request):
    if request.method =='POST':

        contact = Contact()
        contact.Name = request.POST.get('name')
        contact.Email=request.POST.get('email')
        contact.Message=request.POST.get('message')
        contact.save()
        messages.success(request, 'Thanks for connecting to Us! Team will get back to you shortly!!')

    return render(request, 'contact.html')
