from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
import requests

# Create your views here.

CART_SERVICE_URL = "http://cart-service:8002"

class CustomerListCreate(APIView):

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            # Create a cart for the new customer
            requests.post(
                f"{CART_SERVICE_URL}/carts/", json={"customer_id": customer.id}
            )
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
