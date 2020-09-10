from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Recipe(models.Model):
    author = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    ingredients = models.CharField(max_length=1000)
    instructions = models.CharField(max_length=2500)
    photo_url = models.TextField(blank=True)

    def __str__(self):
        return self.name
