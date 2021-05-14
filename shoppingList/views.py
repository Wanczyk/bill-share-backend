from rest_framework import viewsets
from .models import ShoppingList, Item
from .serializers import ShoppingListSerializer, ItemSerializer


class ShoppingListSet(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class ItemSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
