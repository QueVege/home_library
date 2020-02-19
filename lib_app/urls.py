from django.urls import path

from . import views

app_name = "lib"

urlpatterns = [
    path("", views.index, name="index"),
    # path(
    #     'books/',
    #     BooksListView.as_view(),
    #     name='books-list'
    # ),
    # path(
    #     'books/<int:pk>/',
    #     BookDetailView.as_view(),
    #     name='book-detail'
    # ),
    # path(
    #     'authors/<int:pk>/',
    #     AuthorDetailView.as_view(),
    #     name='author-detail'
    # ),
]
