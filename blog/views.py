from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    b_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'b_detail': b_detail})
