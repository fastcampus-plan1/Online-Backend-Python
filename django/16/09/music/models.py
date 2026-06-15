from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='artists/') 
    description = models.TextField()

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='albums/') 
    artist = models.ForeignKey(
        Artist, 
        on_delete=models.CASCADE,
        related_name='albums',
    )
    release_date = models.DateField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("music:album_detail", kwargs={"id": self.pk})
    
    @property
    def url(self):
        return self.get_absolute_url()


class Song(models.Model):
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE, 
        related_name='songs',
    )
    title = models.CharField(max_length=255)
    duration = models.DurationField(default=0)

    def __str__(self):
        return self.title
