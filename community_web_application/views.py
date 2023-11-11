from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def index(request):
    blog_data = Blog.objects.all()[:3]
    return render(request, "community_web_application/index.html",{"blog_data":blog_data})

def all_blogs(request):
    blog_data = Blog.objects.all()
    return render(request, "community_web_application/all_blogs.html",{"blog_data":blog_data})

def contact_us(request):
    return render(request, "contact_us.html")
