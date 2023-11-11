# viewer/urls.py

from django.urls import path
from .views import viewer_signup, viewer_login, viewer_home

urlpatterns = [
    path('signup/', viewer_signup, name='viewer_signup'),
    path('login/', viewer_login, name='viewer_login'),
    path('home/', viewer_home, name='viewer_home'),
    # Add more URL patterns as needed
]
