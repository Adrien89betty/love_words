"""Defines URL patterns for accounts"""
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView, CustomLoginView

app_name = 'user_account'
urlpatterns = [
    # include default auth urls.
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

