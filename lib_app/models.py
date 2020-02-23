from django.db import models
from django.db.models import Max


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} genre"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pen_name = models.CharField(max_length=200)
    year_birth = models.PositiveIntegerField()
    year_death = models.PositiveIntegerField(blank=True, null=True)
    genres = models.ManyToManyField(Genre)
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="authors/")
    biography = models.TextField(max_length=5000)

    def __str__(self):
        return f"{self.pen_name} ({self.first_name} {self.last_name})"

    @property
    def sorted_book_set(self):
        return self.book_set.order_by("year")


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} from {self.country}"


class Book(models.Model):
    class Meta:
        ordering = ["id"]

    authors = models.ManyToManyField(Author, through="BookAuthors",)
    pages = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    publisher = models.ForeignKey(
        Publisher, related_name="books", on_delete=models.CASCADE
    )
    genres = models.ManyToManyField(Genre)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=3000)
    cover = models.ImageField(upload_to="books_covers/")

    def __str__(self):
        return f"{self.title} book"


class BookAuthors(models.Model):
    class Meta:
        ordering = ["order"]
        unique_together = (
            ("book", "author")
        )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        if BookAuthors.objects.filter(book=self.book).count():
            self.order = (
                BookAuthors.objects.filter(book=self.book).latest("order").order + 1
            )
        return super().save(*args, **kwargs)
