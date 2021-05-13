from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import ShoppingList
from .serializers import ShoppingListSerializer


@api_view(['GET', 'POST'])
def shopping_lists(request):
    if request.method == 'GET':
        shoppingLists = ShoppingList.objects.all()
        serializer = ShoppingListSerializer(shoppingLists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ShoppingListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def shopping_list_detail(request, pk):
    try:
        snippet = ShoppingList.objects.get(pk=pk)
    except ShoppingList.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ShoppingListSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShoppingListSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
