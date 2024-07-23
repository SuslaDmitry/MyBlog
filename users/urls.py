"""Определяет схемы URL для пользователей"""
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path, include
from django.urls import path
from . import views

urlpatterns = [
    re_path('login/', LoginView.as_view(template_name='users/login.html'),
         name="login"),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    # Страница регистрации
    re_path(r'^register/$', views.register, name='register'),
]

app_name = "users"
