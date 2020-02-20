import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            "year": ["lt", "gt"],
            "title": ["icontains"],
            "authors__name": ["icontains"],
            "publisher__name": ["icontains"],
        }
