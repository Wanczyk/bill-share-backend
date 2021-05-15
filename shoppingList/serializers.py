from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.item = validated_data.get('item', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


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
        if validated_data.get('name') == instance.name:
            instance.participants.add(request.user)
            try:
                instance.name = request.data['newName']
            except MultiValueDictKeyError:
                pass
            instance.save()
            return instance
        raise ValidationError("Shopping List not exists")
