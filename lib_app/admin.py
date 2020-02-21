from django.contrib import admin

from .models import Author, Book, BookAuthors, Genre, Publisher


class BookAuthorsInline(admin.TabularInline):
    model = BookAuthors
    extra = 1


class BookAdmin(admin.ModelAdmin):
    inlines = (BookAuthorsInline,)


admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
