from django.conf.urls import url

from . import views

app_name='blog'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^archive/$', views.ArchiveView.as_view(), name='archive'),
    url(r'^tech/$', views.tech, name='tech'),
    url(r'^(?P<blog_id>[0-9]+)/comment/$', views.comment, name='comment'),
]