from django.http import HttpResponseRedirect
from .models import Blog, Comment
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
import datetime

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
    
def comment(request, blog_id):
    form_data = request.POST
    blog_obj = get_object_or_404(Blog, pk=blog_id)
    new_comment = Comment(blog=blog_obj, nickname=form_data.__getitem__('nickname'), email=form_data.__getitem__('email'), content=form_data.__getitem__('comment'), pub_date=datetime.datetime.now())
    new_comment.save()
    
    return redirect('blog:detail', pk=blog_id)