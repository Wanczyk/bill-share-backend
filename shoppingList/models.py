import uuid
from django.db import models
from django.contrib.auth.models import User


class ShoppingList(models.Model):
    name = models.CharField(max_length=20)
    participants = models.JSONField()


class Item(models.Model):
    item = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    shoppingList = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
