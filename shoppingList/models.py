from django.db import models
from django.contrib.auth.models import User


class ShoppingList(models.Model):
    name = models.CharField(max_length=20)
    participants = models.ManyToManyField(User, symmetrical=False, blank=False)


class Item(models.Model):
    item = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=50, blank=True)
    shoppingList = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    boughtBy = models.ForeignKey(User, on_delete=models.CASCADE)
