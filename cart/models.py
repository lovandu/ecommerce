from ast import Mod
from operator import mod
from pyexpat import model
from statistics import quantiles
from turtle import update
from django.db import models
from user.models import CustomerUser

# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)

