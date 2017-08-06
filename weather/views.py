from django.shortcuts import render, render_to_response, redirect

from django.template import Template, Context

from django.http import HttpResponse, JsonResponse

from .mods import degree, weather_status, convert_press, city_check

from pyowm import OWM

import json


def weath_info(request):

    API_key = '63ac529deef3fb307c5c5f5d47d4a9de'
    owm = OWM(API_key)
    form = {}
    if request.method == 'POST':
        form['id'] = request.POST.get('id')
        ct = int(form['id'])
        obs = owm.weather_at_id(ct)
        w = obs.get_weather()
        form['stat'] = weather_status(w.get_status())
        form['temperature'] = w.get_temperature('celsius')['temp']
        form['wind_speed'] = w.get_wind()['speed']
        form['wind_der'] = degree(w.get_wind()['deg'])
        form['humidity'] = w.get_humidity()
        form['press'] = convert_press(w.get_pressure()['press'])
        form['city'] = obs.get_location().get_name()
        return JsonResponse(form)
    else:
        return redirect('index_view')


def about(request):

    return render(request, 'other/about.html')

def index(request):

    return render(request, 'other/index.html')

def take_id(request):

    API_key = '63ac529deef3fb307c5c5f5d47d4a9de'
    owm = OWM(API_key)
    form2 = {}
    if request.method == 'POST':
        form2['city'] = request.POST.get('city')
        check_ct = str(form2['city'])
        if city_check(check_ct):
            ct = form2['city']
            obs = owm.weather_at_place(ct)
            w = obs.get_weather()
            form2['Id'] = obs.get_location().get_ID()
        else:
            form2 = {}
        return JsonResponse(form2)
    else:
        return redirect('index_view')
