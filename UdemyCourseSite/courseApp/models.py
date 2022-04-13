from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    instructor = models.CharField(max_length=15)
    rating = models.IntegerField()
