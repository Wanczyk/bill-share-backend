from django.contrib import admin
from .models import ShoppingList, Item


admin.site.register(Item)


class ItemInLine(admin.TabularInline):
    model = Item


@admin.register(ShoppingList)
class ShoppingListInLine(admin.ModelAdmin):
    inlines = [
        ItemInLine
    ]
