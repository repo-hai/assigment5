from django.db import models

# Create your models here.
class Cart(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    customer_ID = models.IntegerField()

class CartItem(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Cart_ID = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    Book_ID = models.IntegerField()
    Quantity = models.IntegerField()