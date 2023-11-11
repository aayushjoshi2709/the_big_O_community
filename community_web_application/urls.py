from . import views
from django.urls import path
urlpatterns = [
    path("", views.index, name="Index"),
    path("blogs", views.all_blogs, name="All Blogs"),
    path("contact-us", views.contact_us,name="contact us"),
    path("blog/<slug:slug>", views.view_blog,name="blog_info")
]