from django.db import models

class Passenger(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=35)
    rewardPoints = models.FloatField()
