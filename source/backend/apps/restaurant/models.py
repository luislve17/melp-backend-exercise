from django.db import models

class Restaurant(models.Model):
    id = models.CharField(max_length=200, primary_key=True) 
    rating = models.IntegerField()
    name = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone  = models.CharField(max_length=100)
    street  = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()