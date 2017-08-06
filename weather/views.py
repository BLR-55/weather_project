from django.shortcuts import render, render_to_response, redirect

from django.template import Template, Context
from django.http import HttpResponse, JsonResponse
import json
from .mods import degree, weather_status
from pyowm import OWM



def weath_info(request):

    API_key = '63ac529deef3fb307c5c5f5d47d4a9de'
    owm = OWM(API_key, language="ru")

    form = {}
    
   
    if request.method == 'POST':
        form['city'] = request.POST.get('city')
        check_ct = str(form['city'])

        if check_ct.isalpha():
            try: 
                ct = form['city']
                obs = owm.weather_at_place(ct)
                w = obs.get_weather()
                form['stat'] = weather_status(w.get_status())
                form['temperature'] = w.get_temperature('celsius')['temp']
                form['wind_speed'] = w.get_wind()['speed']
                form['wind_der'] = degree(w.get_wind()['deg'])
                form['humidity'] = w.get_humidity()
                form['press'] = w.get_pressure()['press'] 



            except: 
                return JsonResponse(form)
        else:
            form = {}

        
        return JsonResponse(form)


    else:
        return redirect('index_view')


def about(request):
    return render(request, 'other/about.html')

def index(request):
    return render(request, 'other/index.html')
































