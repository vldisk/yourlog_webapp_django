"""Определяет схемы URL для пользователей"""

from django.urls import path
from django.contrib.auth.views import login

from . import views


urlpatterns = [
            # Страница входа
            path(r'login/', login, {'template_name': 'users/login.html'},
                                                                name='login'),
            # Страница выхода
            path(r'logout/', views.logout_view, name='logout'),
            # Страница регистрации
            path(r'register/', views.register, name='register'),
            ]
