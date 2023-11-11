from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# artist/models.py

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_or_update_artist_profile(sender, instance, created, **kwargs):
    if created:
        Artist.objects.create(user=instance)
    else:
        instance.artist.save()

class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    #artist = models.CharField(max_length=150)
    title = models.CharField(max_length=255)
   # image = models.ImageField(upload_to='artworks/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
