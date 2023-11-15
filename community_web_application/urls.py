from . import views
from django.urls import path
urlpatterns = [
    path("", views.index, name="Index"),
    path("blogs", views.all_blogs, name="All Blogs"),
    path("contact-us", views.contact_us,name="contact us"),
    path("blog/<slug:slug>", views.view_blog,name="blog_info"),
    path("user/login", views.login, name="Sign In"),
    path("user/register", views.signup_page, name="Join Us"),
    path("user",views.user_actions, name="User_Actions"),
    path("dashboard", views.show_dashboard, name="Dashboad_Index")
]