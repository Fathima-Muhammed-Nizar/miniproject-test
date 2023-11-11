
from .models import Artist,Artwork
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

'''class ArtistSignUpForm(ModelForm):
    class Meta:
        model = Artist
        fields='__all__'''
class ArtistSignUpForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required=True, help_text='Tell us about yourself.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'bio')


class ArtworkForm(ModelForm):
    class Meta:
        model = Artwork
        fields = '__all__'

class ArtistLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())





