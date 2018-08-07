"""Определяет схемы URL для learning_logs."""

from django.urls import path
from . import views


urlpatterns = [
                # Домашняя страница
                path(r'', views.index, name='index'),
                # Вывод всех тем.
                path(r'topics/', views.topics, name='topics'),
                # Страница с подробной информацией по отдельной теме
                path(r'topics/<topic_id>/', views.topic, name='topic'),
                #path(r'topics/(?P<topic_id>\d+)/', views.topic, name='topic')
                # Страница для добавления новой темы
                path(r'new_topic/', views.new_topic, name='new_topic'),
                # Страница для добавления новой записи
                path(r'new_entry/<topic_id>/', views.new_entry, 
                                                    name='new_entry'),
                # Страница для редактирования записи
                path(r'edit_entry/<entry_id>/', views.edit_entry,
                                                    name='edit_entry'),
            ]

