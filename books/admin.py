from django.contrib import admin

from books.models import Genres, Book


admin.site.register(Genres)
admin.site.register(Book)