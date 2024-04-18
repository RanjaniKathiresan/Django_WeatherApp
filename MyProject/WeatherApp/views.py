from django.shortcuts import render
from .form import CityForm
from .models import City
import requests
from django.contrib import messages
# Create your views here.

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},&appid=821793f494008e8e8617f59e9a73211d&units=metric'
    
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            NCity = form.cleaned_data['name']
            CCity = City.objects.filter(name = NCity).count()
            if CCity == 0:
                res = requests.get(url.format(NCity)).json()
                if res['cod'] == 200:
                    form.save()
                    messages.success(request, " "+NCity+" Added Successfully...!!!")
                else:
                    messages.error(request, "City does not exists...!!!")
            else:
                messages.error(request, "City already exists...!!!")

    form = CityForm()
    return render(request, "weatherapp.html", {'form' : form})

