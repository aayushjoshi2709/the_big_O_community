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
    path("dashboard", views.dashboard_home_view, name="dashboard_home"),
    path("dashboard/change-password", views.dashboard_change_password_view, name="dashboard_change_password"),
    path("dashboard/user-info", views.dashboard_user_info_view, name="dashboard_user_info"),
    path("dashboard/your-blog", views.dashboard_your_blog_view, name="dashboard_your_blog"),
    path("dashboard/review-blog", views.dashboard_review_blog_view, name="dashboard_review_blog"),
    path("dashboard/add-blog", views.dashboard_add_blog_view, name="dashboard_add_blog"),
    path("dashboard/image-upload",views.upload_image_view, name="upload_image")
]