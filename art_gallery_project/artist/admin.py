from django.contrib import admin

# Register your models here.
from .models import Artist,Artwork

# Register your models here.
admin.site.register(Artist)
admin.site.register(Artwork)
