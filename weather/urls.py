from django.conf.urls import url

from weather.views import index, weath_info, about

urlpatterns = [
    url(r'^$', index, name='index_view'),
    url(r'^weather_info/$', weath_info),
    url(r'^about/$', about),
]
