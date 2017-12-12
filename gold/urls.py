from django.conf.urls import url, include

from . import views

app_name='gold'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^goldconvert/', include('goldconvert.urls'))
]