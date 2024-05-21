from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
