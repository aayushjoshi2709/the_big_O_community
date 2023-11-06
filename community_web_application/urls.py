from . import views
from django.urls import path
urlpatterns = [
    path("", views.index, name="Index"),
    path("blogs", views.all_blogs, name="All Blogs")
]