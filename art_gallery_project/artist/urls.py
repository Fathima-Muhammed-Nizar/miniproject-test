# artist/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.artist_signup, name='artist_signup'),
    path('login/', views.artist_login, name='artist_login'),
    path('upload/artwork/', views.upload_artwork, name='upload_artwork'),
]
