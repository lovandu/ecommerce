from hashlib import blake2b
from itertools import product
from pickle import TRUE
from pydoc import describe
from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(default='',max_length=255)
    slug=models.CharField(max_length=100, default='')
    description=models.TextField(default='')
    active=models.BooleanField(default=TRUE)

class Product(models.Model):
    title=models.CharField(max_length=255, default='')
    img = models.ImageField(upload_to='product/')
    description=models.TextField(default='')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price= models.IntegerField(default=0)
    active=models.BooleanField(default=True)



