from django.shortcuts import render,get_object_or_404
from .models import Blog
from .forms import LoginForm, RegistrationFrom
import markdown
# Create your views here.
def index(request):
    blog_data = Blog.objects.all()[:4]
    return render(request, "community_web_application/index.html",{"blog_data":blog_data})

def all_blogs(request):
    author_param = request.GET.get('author',None)
    tag_param = request.GET.get('tag', None)
    blog_data = Blog.objects.all()
    if author_param:
        blog_data = blog_data.filter(author=author_param)
    if tag_param:
        blog_data = blog_data.filter(tags__tag__in=[tag_param])
    return render(request, "community_web_application/all_blogs.html",{"blog_data":blog_data})

def contact_us(request):
    return render(request, "contact_us.html")

def view_blog(request,slug):
    # blog_data = Blog.objects.filter(slug=slug))
    blog_data = get_object_or_404(Blog, slug = slug)
    blog_data.content = markdown.markdown(blog_data.content)
    return render(request, "community_web_application/blog.html",{"blog_data":blog_data})

def login(request):
    login_form = LoginForm()
    return render(request,"community_web_application/user/login.html",{"login_form":login_form})

def signup_page(request):
    registration_form = RegistrationFrom()
    return render(request,"community_web_application/user/register.html",{"registration_form":registration_form})


def user_actions(request):
    pass