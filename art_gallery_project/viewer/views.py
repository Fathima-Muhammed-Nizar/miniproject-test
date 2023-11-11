

# Create your views here.
# viewer/views.py

# viewer/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from artist.models import Artwork,Artist

from .forms import ViewerSignUpForm

def viewer_signup(request):
    if request.method == 'POST':
        form = ViewerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('viewer_home')
    else:
        form = ViewerSignUpForm()
    return render(request, 'viewer/viewer_signup.html', {'form': form})

def viewer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('viewer_home')
    else:
        form = AuthenticationForm()
    return render(request, 'viewer/viewer_login.html', {'form': form})

@login_required
def viewer_home(request):
    artworks = Artwork.objects.all()
    return render(request, 'viewer/viewer_home.html', {'artworks': artworks})
