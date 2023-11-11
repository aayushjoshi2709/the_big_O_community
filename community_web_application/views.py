from django.shortcuts import render,get_object_or_404
from django.forms.models import model_to_dict
from django.http import HttpResponse
from .models import Blog,Author
import markdown
# Create your views here.
def index(request):
    blog_data = Blog.objects.all()[:3]
    return render(request, "community_web_application/index.html",{"blog_data":blog_data})

def all_blogs(request):
    blog_data = Blog.objects.all()
    return render(request, "community_web_application/all_blogs.html",{"blog_data":blog_data})

def contact_us(request):
    return render(request, "contact_us.html")

def view_blog(request,slug):
    # blog_data = Blog.objects.filter(slug=slug))
    blog_data = get_object_or_404(Blog, slug = slug)
    blog_data.content = markdown.markdown(blog_data.content)
    return render(request, "community_web_application/blog.html",{"blog_data":blog_data})
