from django.urls import path

from . import views

urlpatterns = [
    path("register_users/", views.register_user, name="register_users"),
    path("create_blog/", views.create_blog, name="create_blog"),
]
