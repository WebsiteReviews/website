from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from books.models import Book, Genres, Review
from .forms import ReviewForm
# Create your views here.

def main(request):
    six_books = Book.objects.all()[:6]
    context = {'title':'AboutBooooks',
               'username':'arseniy',
               'six_books': six_books,
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
    reviews = Review.objects.filter(book=book)

    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            if request.user.is_authenticated:
                text = review_form.cleaned_data['review_text']
                Review.objects.create(user=request.user, book=book, text=text)
                return HttpResponseRedirect(request.path_info)
            else:
                return HttpResponseRedirect(reverse('users:enter_or_registration'))

    context = {
        'book': book,
        'reviews':reviews,
        'review_form':review_form,
    }
    return render(request, 'books/page_of_book.html', context)
