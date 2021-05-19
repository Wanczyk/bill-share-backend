from rest_framework import viewsets, generics
from .models import ShoppingList, Item
from .permissions import IsCreatorOrReadOnly, IsParticipant
from .serializers import ShoppingListSerializer, ItemSerializer


class ShoppingListJoin(generics.UpdateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class ShoppingListSet(viewsets.ModelViewSet):
    permission_classes = (IsParticipant,)
    http_method_names = ['get', 'post']
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class ItemSet(viewsets.ModelViewSet):
    permission_classes = (IsCreatorOrReadOnly,)
    http_method_names = ['get', 'post', 'path', 'delete']
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
