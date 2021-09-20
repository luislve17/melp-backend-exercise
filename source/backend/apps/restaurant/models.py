from django.db import models
import uuid

class Restaurant(models.Model):
    # id = models.CharField(max_length=200, primary_key=True) 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    site = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone  = models.CharField(max_length=100, null=True)
    street  = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)