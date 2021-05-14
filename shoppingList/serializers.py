from rest_framework import serializers
from .models import ShoppingList, Item
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        model = User


class ItemSerializer(serializers.ModelSerializer):
    boughtBy = UserSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Item

    def create(self, validated_data):
        request = self.context.get('request')
        item = Item.objects.create(
            item=request.data['item'],
            description=request.data['item'],
            shoppingList=ShoppingList.objects.get(pk=request.data['shoppingList']),
            price=request.data['price'],
            boughtBy=request.user
        )
        item.save()
        return item


class ShoppingListSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = ShoppingList

    def create(self, validated_data):
        request = self.context.get('request')
        shopping_list = ShoppingList.objects.create(name=request.data['name'])
        shopping_list.participants.add(request.user)
        shopping_list.save()
        return shopping_list

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.participants.add(request.user)
        instance.save()
        return instance
