from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "community_web_application/index.html",{})

def all_blogs(request):
    return render(request, "community_web_application/all_blogs.html",{})

def contact_us(request):
    return render(request, "contact_us.html")
