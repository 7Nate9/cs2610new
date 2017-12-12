from django.conf.urls import url

from . import views

app_name='goldconvert'

urlpatterns = [
    url(r'^\?from=(?P<fromUnit>.+)&to=(?P<toUnit>.+)&value=(?P<weight>\d+.?\d*)$', views.conversion, name='conversion'),
    url(r'^', views.conversion, name="testing2"),
    url(r'^testing$', views.testing, name="testing")
]