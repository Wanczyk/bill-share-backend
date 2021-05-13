from rest_framework import serializers
from .models import ShoppingList


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'participants')
        model = ShoppingList
