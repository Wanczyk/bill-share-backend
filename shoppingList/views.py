from rest_framework import viewsets
from .models import ShoppingList, Item
from .serializers import ShoppingListSerializer, ItemSerializer


class ShoppingListSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put']
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class ItemSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'path', 'delete']
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
