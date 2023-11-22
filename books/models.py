from django.db import models

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


