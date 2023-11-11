

# Create your views here.
# artist/views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArtistSignUpForm, ArtworkForm,ArtistLoginForm
from .models import Artwork, Artist
from django.contrib import messages
from django.http import HttpResponse

def artist_signup(request):
    if request.method == 'POST':
        form = ArtistSignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return HttpResponse('/artist/login/')# Replace with the actual login URL
    else:
        form = ArtistSignUpForm()
    return render(request, 'artist/artist_signup.html', {'form': form})

def artist_login(request):
    # Implementation for artist login
    if request.method == 'POST':
        form = ArtistLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return HttpResponse("You logged in")  # Replace with the actual login URL
    
                #return redirect('home')  # Replace 'home' with your desired URL after login
            else:
                messages.error(request, 'Invalid username or password.')

    else:
        form = ArtistLoginForm()
    return render(request, 'artist/artist_login.html', {'form': form})




def upload_artwork(request):
    
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user.artist
            artwork.save()
            return HttpResponse("Please Try Again!!")
            #return redirect('view_artworks')  # Replace with the actual view artworks URL
    else:
        form = ArtworkForm()
    return render(request, 'artist/upload_artwork.html', {'form': form})

