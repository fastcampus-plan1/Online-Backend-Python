from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    copies_sold = models.PositiveIntegerField(default=0)
