from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodMenu 

def home(request):
    items = FoodMenu.objects.all()
    return render(request,'myapp/home.html',{'items':items})

