from django.urls import path

from . import views

app_name = "lib"

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.BooksListView.as_view(), name="books-list"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book-details"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author-details"),
]
