# Create your models here.
from django.db import models

class Distributor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return '%s - %s - %s' % (self.name, self.city, self.country)

class Device(models.Model):
    name = models.CharField(max_length=30)
    typename = models.CharField(max_length=40)
    price = models.IntegerField()

    def __str__(self):
        return '%s - %s$' % (self.name, self.price)

class Comment(models.Model):
    commentId = models.CharField(max_length=100)
    content = models.CharField(max_length=1000, default="")

    def __str__(self):
        return '%s' % (self.commentId)