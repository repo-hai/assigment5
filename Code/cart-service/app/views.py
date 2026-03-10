from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer 
import requests

# Create your views here.
BOOK_SERVICE_URL = 'http://book-servicec:8001'

class CartCreate(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class AddCartItem(APIView):
    def post(self, request):
        book_id = request.data["book_id"]

        r = requests.get(f"{BOOK_SERVICE_URL}/books/")
        books = r.json()
        
        if not any(book['id'] == book_id for book in books):
            return Response({"error": "Book not found"}, status=404)
        
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": "CartItem not found"}, status=400)
    
class ViewCart(APIView):
    def get(self, request, customer_id):
        try:
            cart = Cart.objects.get(customer_id=customer_id)
            items = CartItem.objects.filter(cart=cart)
            serializer = CartItemSerializer(items, many=True)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found"}, status=404)