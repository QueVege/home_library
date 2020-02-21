import django_filters
from django.db.models import Max, Min

from .models import Book


class CustomOrderingFilter(django_filters.OrderingFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra["choices"] += [
            ("author", "Author"),
            ("-author", "Author (descending)"),
        ]

    def filter(self, qs, value):
        if any(v in ["author", "-author"] for v in value):
            return qs.annotate(author=Min("bookauthors__order")).order_by(*value)
        return super().filter(qs, value)


class BookFilter(django_filters.FilterSet):

    ordering = CustomOrderingFilter(fields=(("year", "year"), ("title", "title"),))

    class Meta:
        model = Book
        fields = {
            "year": ["lt", "gt"],
            "title": ["icontains"],
            "authors__name": ["icontains"],
            "publisher__name": ["icontains"],
        }
