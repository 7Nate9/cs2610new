from django.conf.urls import url

from . import views

app_name='gold'

urlpatterns = [
    url(r'^\?from=(?P<fromUnit>.+)&to=(?P<toUnit>.+)&value=(?P<weight>\d+.?\d*)$', views.conversion, name='conversion')
]