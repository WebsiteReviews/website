from django.contrib import admin

from books.models import Genres, Book, Review


admin.site.register(Genres)
admin.site.register(Book)
admin.site.register(Review)