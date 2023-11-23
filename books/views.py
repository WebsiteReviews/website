from django.shortcuts import render, get_object_or_404

from books.models import Book, Genres
# Create your views here.

def main(request):
    context = {'title':'AboutBooooks',
               'username':'arseniy'
               }
    return render(request, 'books/main.html', context)


def catalog(request,category_id = None):
    genres = Genres.objects.all()
    genre_dict = {'Фентези': 'fantasy', 'Романы': 'romans', 'Драмы':'dramas', 'Приключения':'adventures', 'Наука':'science'}

    for genre in genres:
        genre.name_in_english = genre_dict.get(genre.name, '')

    if category_id and category_id != 'all':
        books = Book.objects.filter(genre_id=category_id)
    else:
        books = Book.objects.all()

    context = {
        'title': 'Каталог книг',
        'books': books,
        'genres': genres,
        'genre_dict': genre_dict,
    }

    return render(request,'books/catalog.html', context)


def page_of_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'books/page_of_book.html', context)
