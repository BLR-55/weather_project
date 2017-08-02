from django.conf.urls import url

from weather.views import index, weath2, weath_info

urlpatterns = [
    url(r'^$', index, name='index_view'),
    url(r'^test/$', weath2),
    url(r'^weather_info/$', weath_info),
]
