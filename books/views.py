from django.shortcuts import render

from books.models import Book, Genres
# Create your views here.

def main(request):
    context = {'title':'AboutBooooks',
               'username':'arseniy'
               }
    return render(request, 'books/main.html', context)


def catalog(request):
    genres = Genres.objects.all()
    genre_dict = {'Фентези': 'fantasy', 'Романы': 'romans', 'Драмы':'dramas', 'Приключения':'adventures', 'Наука':'science'}

    for genre in genres:
        genre.name_in_english = genre_dict.get(genre.name, '')

    context = {
        'title': 'Каталог книг',
        'books': Book.objects.all(),
        'genres': genres,
        'genre_dict': genre_dict,
    }

    return render(request,'books/catalog.html', context)

