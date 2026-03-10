from django.shortcuts import render
import requests

BOOK_SERVICE_URL = "http://book-service:8001"

def book_list(request):
    r = requests.get(f"{BOOK_SERVICE_URL}/books/")
    return render(request, "books.html", {"books": r.json()})

def view_cart(request, customer_id):
    r = requests.get(f"{BOOK_SERVICE_URL}/cart/{customer_id}/")
    return render(request, "cart.html", {"cart": r.json()})