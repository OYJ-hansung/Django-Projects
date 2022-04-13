from django.db import models

# Create your models here.
class Movie(models.Model):
    releaseDate = models.DateField()
    title = models.CharField(max_length=30)
    rating = models.IntegerField()
