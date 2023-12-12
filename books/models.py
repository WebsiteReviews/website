from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
# Create your models here.

class Genres(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    publication_date = models.CharField(max_length=16, default='')
    image_link = models.TextField(default='')
    synonpis = models.TextField(default='')
    excerpt = models.TextField(default='')
    genre = models.ForeignKey(to=Genres, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Рецензию оставил {self.user.username} на книгу {self.book.title}"

