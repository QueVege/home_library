from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Author, Book


def index(request):
    return HttpResponse("Hello")


class BooksListView(ListView):
    model = Book
    template_name = "lib/books_list.html"
    context_object_name = "books"
    paginate_by = 3


class BookDetailView(DetailView):
    model = Book
    template_name = "lib/book_details.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class AuthorDetailView(DetailView):
    model = Author
    template_name = "lib/author_details.html"
