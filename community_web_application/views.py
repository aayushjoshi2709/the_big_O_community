from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Blog, Author
from .forms import LoginForm, RegistrationFrom
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import markdown
# Create your views here.
def index_view(request):
    blog_data = Blog.objects.all()[:4]
    return render(request, "community_web_application/index.html",{"blog_data":blog_data})

def all_blogs_view(request):
    author_param = request.GET.get('author',None)
    tag_param = request.GET.get('tag', None)
    blog_data = Blog.objects.all()
    if author_param:
        blog_data = blog_data.filter(author=author_param)
    if tag_param:
        blog_data = blog_data.filter(tags__tag__in=[tag_param])
    return render(request, "community_web_application/all_blogs.html",{"blog_data":blog_data})

def contact_us_view(request):
    return render(request, "contact_us.html")

def view_blog_view(request,slug):
    # blog_data = Blog.objects.filter(slug=slug))
    blog_data = get_object_or_404(Blog, slug = slug)
    blog_data.content = markdown.markdown(blog_data.content)
    return render(request, "community_web_application/blog.html",{"blog_data":blog_data})

def login_view(request):
    stored_messages = messages.get_messages(request)
    login_form = LoginForm()
    if request.method == "GET":
        return render(request,"community_web_application/user/login.html",{"login_form":login_form, "messages":stored_messages})
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        author = authenticate(request, username=username, password=password)
        if author is not None:
            login(request, author)
            return HttpResponseRedirect(reverse('dashboad_index'))
        else:
            messages.add_message(request,messages.ERROR, "Username or password not correct")
            return HttpResponseRedirect(reverse("sign_in"))

def signup_page_view(request):
    stored_messages = messages.get_messages(request)
    registration_form = RegistrationFrom()
    return render(request,"community_web_application/user/register.html",{"registration_form":registration_form, "messages":stored_messages})

def show_dashboard_view(request):
    return render(request, "community_web_application/dashboard/home.html")

def user_actions_view(request):
    if request.method == "POST":
        registration_form = RegistrationFrom(request.POST)
        print(registration_form.is_valid())
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            raw_password = registration_form.cleaned_data.get('password1')
            author = authenticate(username=username, password=raw_password)
            login(request,author)
            return HttpResponseRedirect(reverse('dashboad_index'))
        else:
            for field, errors in registration_form.errors.items():
                for error in errors:
                    messages.add_message(request, messages.ERROR, error)
            return HttpResponseRedirect(reverse('join_us'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
