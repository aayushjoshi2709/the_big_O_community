from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Blog, Image,Author,TeamMembers
from .forms import LoginForm, RegistrationFrom, RegistrationUpdationForm, UpdatePasswordForm,AddBlogForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.core.files import File
import json
# Create your views here.s
@require_http_methods(["GET"])
def index_view(request):
    blog_data = Blog.objects.all()[:4]
    return render(request, "community_web_application/index.html",{"blog_data":blog_data})

@require_http_methods(["GET"])
def all_blogs_view(request):
    author_param = request.GET.get('author',None)
    tag_param = request.GET.get('tag', None)
    blog_data = Blog.objects.all()
    if author_param:
        blog_data = blog_data.filter(author=author_param)
    if tag_param:
        blog_data = blog_data.filter(tags__tag__in=[tag_param])
    return render(request, "community_web_application/all_blogs.html",{"blog_data":blog_data})

@require_http_methods(["GET"])
def contact_us_view(request):
    return render(request, "contact_us.html")

@require_http_methods(["GET"])
def view_blog_view(request,slug):
    blog_data = get_object_or_404(Blog, slug = slug)
    blog_data.content = blog_data.content
    return render(request, "community_web_application/blog.html",{"blog_data":blog_data})


@require_http_methods(["GET"])
def our_team_view(request):
    members = TeamMembers.objects.all()
    return render(request, "community_web_application/our_team.html", {
        "members":members
    })




@require_http_methods(["GET", "POST"])
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
            return HttpResponseRedirect(reverse('dashboard_home'))
        else:
            messages.add_message(request,messages.ERROR, "Username or password not correct")
            return HttpResponseRedirect(reverse("sign_in"))

@require_http_methods(["GET", "POST"])
def signup_page_view(request):
    if request.method == "GET":
        stored_messages = messages.get_messages(request)
        registration_form = RegistrationFrom()
        return render(request,"community_web_application/user/register.html",{"registration_form":registration_form, "messages":stored_messages})
    elif request.method == "POST":
        registration_form = RegistrationFrom(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            raw_password = registration_form.cleaned_data.get('password1')
            author = authenticate(username=username, password=raw_password)
            login(request,author)
            return HttpResponseRedirect(reverse('dashboard_home'))
        else:
            for field, errors in registration_form.errors.items():
                for error in errors:
                    messages.add_message(request, messages.ERROR, error)
            return HttpResponseRedirect(reverse('join_us'))

@require_http_methods(["GET"])
def dashboard_home_view(request):
    if request.user.is_authenticated:
        return render(request, "community_web_application/dashboard/home.html")
    else:
        messages.add_message(request,messages.ERROR, "Please sign in first")
        return HttpResponseRedirect(reverse("sign_in"))

@require_http_methods(["GET", "POST"])
def dashboard_user_info_view(request):
    stored_messages = messages.get_messages(request)
    if request.user.is_authenticated:
        if request.method =="GET":
            registration_updation_form = RegistrationUpdationForm(initial={
                "first_name":request.user.first_name,
                "last_name":request.user.last_name,
                "username":request.user.username,
                "email":request.user.email
            })
            return render(request, "community_web_application/dashboard/user_info.html", {"form":registration_updation_form, "messages":stored_messages})
        elif request.method == "POST":
            registration_updation_form = RegistrationUpdationForm(request.POST, instance=request.user)
            if registration_updation_form.is_valid():
                registration_updation_form.save()
                messages.success(request, 'Author information updated successfully.')
            else:
                for field, errors in registration_updation_form.errors.items():
                    for error in errors:
                        messages.add_message(request, messages.ERROR, error)
            return HttpResponseRedirect(reverse('dashboard_user_info'))   
    else:
        messages.add_message(request,messages.ERROR, "Please sign in first")
        return HttpResponseRedirect(reverse("sign_in"))

@require_http_methods(["GET"])
def dashboard_review_blog_view(request):
    if request.user.is_authenticated:
        return render(request, "community_web_application/dashboard/review_blog.html")
    else:
        messages.add_message(request,messages.ERROR, "Please sign in first")
        return HttpResponseRedirect(reverse("sign_in"))

@require_http_methods(["GET"])
def dashboard_your_blog_view(request):
    if request.user.is_authenticated:
        stored_messages = messages.get_messages(request)
        blogs = Blog.objects.filter(author=request.user)
        return render(request, "community_web_application/dashboard/your_blogs.html", {"blogs":blogs,"messages":stored_messages})
    else:
        messages.add_message(request,messages.ERROR, "Please sign in first")
        return HttpResponseRedirect(reverse("sign_in"))

@require_http_methods(["GET", "POST"])
def dashboard_update_blog_view(request,id):
    stored_messages = messages.get_messages(request)
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, pk=id,author=request.user) 
        if request.method == "GET":
            add_blog = AddBlogForm(instance=blog)
            return render(request, "community_web_application/dashboard/update_blog.html",{"blog":blog,"form":add_blog, "messages":stored_messages})
        elif request.method == "POST":
            add_blog_form = AddBlogForm(request.POST, instance=blog)
            if add_blog_form.is_valid():
                blog = add_blog_form.save(commit=False)
                blog.author = Author.objects.get(pk=request.user.id)                
                blog.save()
                add_blog_form.save_m2m()
                messages.add_message(request, messages.SUCCESS, 'Blog updated successfully')
                return HttpResponseRedirect(reverse('dashboard_your_blog'))
            else:
                for field, errors in add_blog_form.errors.items():
                    for error in errors:
                        messages.add_message(request, messages.ERROR, error)
                return HttpResponseRedirect(reverse('dashboard_update_blog'))
    else:
        messages.add_message(request,messages.ERROR, "Please sign in first")
        return HttpResponseRedirect(reverse("sign_in"))

@require_http_methods(["GET", "POST"]) 
def dashboard_add_blog_view(request):
    stored_messages = messages.get_messages(request)
    if request.user.is_authenticated:
        if request.method == "GET":
            add_blog = AddBlogForm()
            return render(request, "community_web_application/dashboard/add_blog.html",{"form":add_blog, "messages":stored_messages})
        elif request.method == "POST":
            add_blog_form = AddBlogForm(request.POST)
            if add_blog_form.is_valid():
                blog = add_blog_form.save(commit=False)
                blog.author = Author.objects.get(pk=request.user.id)                
                blog.save()
                add_blog_form.save_m2m()
                messages.add_message(request, messages.SUCCESS, 'Blog added successfully')
                return HttpResponseRedirect(reverse('dashboard_add_blog'))
            else:
                for field, errors in add_blog_form.errors.items():
                    for error in errors:
                        messages.add_message(request, messages.ERROR, error)
                return HttpResponseRedirect(reverse('dashboard_add_blog'))
    else:
        messages.add_message(request,messages.ERROR, "Please sign in first")
        return HttpResponseRedirect(reverse("sign_in"))

@require_http_methods(["GET", "POST"]) 
def dashboard_change_password_view(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            update_password_form = UpdatePasswordForm(user=request.user)
            return render(request, "community_web_application/dashboard/change_password.html", {"form":update_password_form})
        elif request.method == "POST":
            update_password_form = UpdatePasswordForm(request.user, request.POST)
            if update_password_form.is_valid():
                user = update_password_form.save()
                update_session_auth_hash(request, user)
                messages.add_message(request, messages.SUCCESS, "Password updated successfully..")
            else:
                for field, errors in update_password_form.errors.items():
                    for error in errors:
                        messages.add_message(request, messages.ERROR, error)
            return HttpResponseRedirect(reverse('dashboard_change_password'))
    else:
        messages.add_message(request,messages.ERROR, "Please sign in first")
        return HttpResponseRedirect(reverse("sign_in"))

@require_http_methods(["POST"])
def dashboard_user_delete_view(request):
    if request.user.is_authenticated:
        author = get_object_or_404(Author, pk=request.user.id)
        author.delete()
        logout(request)
        messages.add_message(request,messages.SUCCESS, "User deleted successfully")
        return HttpResponseRedirect(reverse("sign_in"))
    else:
        messages.add_message(request,messages.ERROR, "Please sign in first")
        return HttpResponseRedirect(reverse("sign_in"))

@require_http_methods(["POST"])
def dashboard_blog_delete_view(request):
    if request.user.is_authenticated:
        blog_id = json.loads(request.body)['blog_id']
        blog = get_object_or_404(Blog, pk=blog_id, author=request.user)
        blog.delete()
        messages.add_message(request,messages.SUCCESS, "Blog deleted successfully")
        return HttpResponseRedirect(reverse("dashboard_your_blog"))
    else:
        messages.add_message(request,messages.ERROR, "Please sign in first")
        return HttpResponseRedirect(reverse("sign_in"))


@csrf_exempt
def upload_image_view(request):
    if request.user.is_authenticated:
        image = Image()
        image_file = request.FILES['upload']
        image.author = Author.objects.get(pk=request.user.id)
        image.image.save(image_file.name, File(image_file))
        image.save()
        url = request.build_absolute_uri(image.image.url)
        print(url)
        return JsonResponse({
            "uploaded": 1,
            "fileName": image.image.name,
            'url': url
        })
    else:
        messages.add_message(request,messages.ERROR, "Please sign in first")
        return HttpResponseRedirect(reverse("sign_in"))

@require_http_methods(["GET"])
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
