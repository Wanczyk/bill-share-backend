from django.urls import path, include
from .views import ShoppingListSet, ItemSet, ShoppingListJoin
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'shoppingList', ShoppingListSet, basename='shopping_list')
router.register(r'item', ItemSet, basename='item')

urlpatterns = [
    path('shoppingList/<int:pk>/join', ShoppingListJoin.as_view())
]

urlpatterns += router.urls

