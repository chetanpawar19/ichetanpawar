from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blog = Blog.objects
    return render(request, 'blog/allblogs.html',{'blog':blog})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)  #pk primary
    return render(request, 'blog/detailblog.html', {'blog':detailblog})