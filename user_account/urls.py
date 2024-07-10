"""Defines URL patterns for accounts"""

from django.urls import path, include

app_name = 'user_account'
urlpatterns = [
    # include default auth urls.
    path('', include('django.contrib.auth.urls')),
]
