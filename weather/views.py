from django.shortcuts import render, render_to_response, redirect

from django.template import Template, Context
from django.http import HttpResponse, JsonResponse
import json

from pyowm import OWM



def weath_info(request):

    API_key = '63ac529deef3fb307c5c5f5d47d4a9de'
    owm = OWM(API_key)

    errors = []
    form = {}
   
    if request.method == 'POST':
        print(3)
        form['city'] = request.POST.get('city')
        try: 
            ct = form['city']
            obs = owm.weather_at_place(ct)
            w = obs.get_weather()
            form['temperature'] = w.get_temperature('celsius')['temp']
            form['wind_speed'] = w.get_wind()['speed']
            form['humidity'] = w.get_humidity()
            form['press'] = w.get_pressure()['press'] 


        except:
            print(4)
            return render(request, 'other/weather_info.html', {'message': 'Такого города нет'})

        return HttpResponse(json.dumps(form))
        # #return render(request, 'other/weather_info.html', {'city':ct, 'temp':form['temperature'],\
        #                                         'wind_s':form['wind_speed'], 'humidity':form['humidity'],\
        #                                         'press':form['press']}\
        #                                         )
    else:
        print(11)
        return redirect('index_view')
        # html = "<html><body>Блок елсе</body></html>"
        # return HttpResponse(html)

def index(request):
    return render(request, 'other/index.html')




























# def weath_info(request):

#     API_key = 'code here'
#     owm = OWM(API_key)

#     errors = []
#     form = {}
#     if request.method == 'POST':
#         form['city'] = request.POST.get('city')
        

#         if not form['city']:
#             errors.append('Введите город')

#             t = Template("<html><body>В Москве сейчас {{temperature}} по цельсию, давление : {{pressure}} мм рт ст.</body></html>")
#             html = t.render(Context({'temperature': 10, 'pressure': 20}))
#             return HttpResponse(html)

#         else:
#             try: 
#                 ct = form['city']
#                 obs = owm.weather_at_place(ct)
#                 w = obs.get_weather()
#                 form['temperature'] = w.get_temperature('celsius')['temp']
#                 form['wind_speed'] = w.get_wind()['speed']
#                 form['humidity'] = w.get_humidity()
#                 form['press'] = w.get_pressure()['press'] 

#             except:
#                 html = "<html><body>Такого города нет</body></html>"
#                 return HttpResponse(html)




      

#             return render(request, 'other/weather_info.html', {'errors':errors, 'city':ct, 'temp':form['temperature'],\
#                                                 'wind_s':form['wind_speed'], 'humidity':form['humidity'],\
#                                                 'press':form['press']}\
#                                                 )
#     else:
#         t = Template("<html><body>В Москве сейчас {{temperature}} по цельсию, давление : {{pressure}} мм рт ст.</body></html>")
#         html = t.render(Context({'temperature': 10, 'pressure': 20}))
#         return HttpResponse(html)
        # return render(request, 'other/weather_info.html')









