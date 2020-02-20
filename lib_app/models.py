from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} genre"


class Author(models.Model):
    name = models.CharField(max_length=300)
    pen_name = models.CharField(max_length=300)
    year_birth = models.IntegerField()
    year_death = models.IntegerField(blank=True, null=True)
    genres = models.ManyToManyField(Genre)
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="authors/")
    biography = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.pen_name} ({self.name})"

    @property
    def sorted_book_set(self):
        return self.book_set.order_by("year")


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} from {self.country}"


class Book(models.Model):
    authors = models.ManyToManyField(Author)
    pages = models.IntegerField()
    year = models.IntegerField()
    publisher = models.ForeignKey(
        Publisher, related_name="books", on_delete=models.CASCADE
    )
    genres = models.ManyToManyField(Genre)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    cover = models.ImageField(upload_to="books_covers/")

    def __str__(self):
        return f"{self.title} book"
