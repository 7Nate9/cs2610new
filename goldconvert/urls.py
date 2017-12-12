from django.conf.urls import url

from . import views

app_name='goldconvert'

urlpatterns = [
    url(r'^', views.conversion, name="conversion")
]