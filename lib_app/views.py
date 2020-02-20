from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django_filters.views import FilterView

from .filters import BookFilter
from .models import Author, Book


def index(request):
    return HttpResponse("Hello")


class BooksListView(FilterView):
    model = Book
    template_name = "lib/books_list.html"
    context_object_name = "books"
    filterset_class = BookFilter
    paginate_by = 30


class BookDetailView(DetailView):
    model = Book
    template_name = "lib/book_details.html"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "lib/author_details.html"
