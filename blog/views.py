from django.http import HttpResponseRedirect
from .models import Blog, Comment
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

class HomeView(generic.ListView):
    template_name='blog/home.html'
    context_object_name='latest_blog_list'
    
    def get_queryset(self):
        return Blog.objects.order_by('-pub_date')[:3]

class ArchiveView(generic.ListView):
    template_name='blog/archive.html'
    context_object_name='blog_list'
    
    def get_queryset(self):
        return Blog.objects.order_by('-pub_date')
        
class DetailView(generic.DetailView):
    model=Blog
    template_name='blog/detail.html'
    
def tech(request):
    return render(request, 'blog/tech.html')
    
def about(request):
    return render(request, 'blog/about.html')