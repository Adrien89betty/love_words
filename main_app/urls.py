"""Defines URL patterns for main_app."""
from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    path('new_profile/', views.new_profile, name='new_profile'),
    path('profile/', views.show_profile, name='show_profile'),
    path('new_profile/', views.new_profile, name='new_profile'),
]
