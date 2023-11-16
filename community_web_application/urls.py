from . import views
from django.urls import path
urlpatterns = [
    path("", views.index_view, name="index"),
    path("blogs", views.all_blogs_view, name="all_blogs"),
    path("contact-us", views.contact_us_view,name="contact_us"),
    path("blog/<slug:slug>", views.view_blog_view,name="blog_info"),
    path("user/login", views.login_view, name="sign_in"),
    path("user/register", views.signup_page_view, name="join_us"),
    path("user/logout", views.logout_view, name="logout"),
    path("user",views.user_actions_view, name="user_actions"),
    path("dashboard", views.show_dashboard_view, name="dashboad_index")

]