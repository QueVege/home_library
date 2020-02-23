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

    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    year__gt = django_filters.NumberFilter(field_name='year', lookup_expr='gt', label='From')
    year__lt = django_filters.NumberFilter(field_name='year', lookup_expr='lt', label='To')
    authors = django_filters.CharFilter(field_name='authors__last_name', lookup_expr='icontains', label='Author')
    publisher = django_filters.CharFilter(field_name='publisher__name', lookup_expr='icontains', label='Publisher')


    # ordering = CustomOrderingFilter(fields=(("year", "year"), ("title", "title"),))

    class Meta:
        model = Book
        fields = []
