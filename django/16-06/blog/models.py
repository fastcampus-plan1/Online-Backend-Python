from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='posts',
        null=True,
    )
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    file = models.FileField(upload_to='posts/files/', null=True, blank=True)

    def __str__(self):
        return self.title
