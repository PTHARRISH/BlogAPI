from django.urls import path

from . import views

urlpatterns = [
    path("register_users/", views.register_user, name="register_users"),
    path("create_blog/", views.create_blog, name="create_blog"),
    path("blog_list/", views.blog_list, name="blog_list"),
    path("update_blog/<int:pk>", views.update_blog, name="update_blog"),
]
