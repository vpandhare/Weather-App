from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
import urllib.request
import json

def index(request):
    return render(request,'index.html')

def index(request):
    if request.method =='POST':
        city = request.POST['city']
        city= city.replace(' ','+')
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=weather+in+{city}=4605d4f6eb5f5adee67046410943a044').text()
        list_of_data =json.loads(source)
        
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['icon']) + str(list_of_data['coord']['lat']),
            "temp" : str(list_of_data['main']['temp'])+'°C',
            "pressure": str(list_of_data['main']['pressur']),
            "humidity": str(list_of_data['main']['humidity']),
            "main" : str(list_of_data['weather'][0]['main']),
            "discription":str(list_of_data['weather'][0]['description']),
            "icon": list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data={}

    return render (request,"main/index.html",data)

