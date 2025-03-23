from django.shortcuts import render
from django.contrib import messages
import datetime
import requests

def home(request):
    
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='indore'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=39d64488917224b8adfec85224fb5a31'
    PARAMS= {'units':'metric'}
    
    description=""
    icon=""
    temp=""
    exception_occurred=""
    
    try:
      data=requests.get(url,params=PARAMS).json()

      description = data['weather'][0]['description']
      icon = data['weather'][0]['icon']
      temp = data['main']['temp']

      day = datetime.date.today()

      return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occurred':False})
   
    
    except requests.exceptions.RequestException:
      exception_occurred=True
      messages.error(request,'entered data is not avilable to API')
    
    except KeyError:
      exception_occurred= True
      messages.error(request,"Unexpected data formate from the API")
      
    day=datetime.date.today()

    return render(request,'weatherapp/index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':exception_occurred})