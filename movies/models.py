from django.db import models

# Create your models here.
from django.db import models
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.URLField()
    genres = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    year_release = models.PositiveIntegerField()
    metacritic_rating = models.PositiveIntegerField()
    runtime = models.PositiveIntegerField()

    def __str__(self):
        return self.title