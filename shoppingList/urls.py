from django.urls import path
from .views import shopping_lists, shopping_list_detail

urlpatterns = [
    path('', shopping_lists),
    path('<int:pk>/', shopping_list_detail),
]
