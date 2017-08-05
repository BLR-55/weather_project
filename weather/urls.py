from django.conf.urls import url

from weather.views import index, weath_info, new_form

urlpatterns = [
    url(r'^$', index, name='index_view'),
    url(r'^weather_info/$', weath_info),
    url(r'^new_form/$', new_form),
]
