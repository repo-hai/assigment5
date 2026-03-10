from django.db import models

# Create your models here.
class Salecode(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Code = models.CharField(max_length=255)
    Created_at = models.DateTimeField(auto_now_add=True)
    Start_Day = models.DateTimeField(auto_now_add=True)
    End_Day = models.DateTimeField(auto_now_add=True)
    Discount = models.FloatField()

    def __str__(self):
        return self.ID

class Customer_salecode(models.Model):
    pk = models.CompositePrimaryKey('Customer_ID', 'Salecode_ID')
    Customer_ID = models.CharField(max_length=255, unique=True)
    Salecode_ID = models.ForeignKey(Salecode, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.ID
    
class Salecode_Order(models.Model):
    pk = models.CompositePrimaryKey('Order_ID', 'Customer_ID', 'Salecode_ID')
    Order_ID = models.CharField(max_length=255, unique=True)
    Customer_ID = models.CharField(max_length=255)
    Salecode_ID = models.CharField(max_length=255)
    Customer_salecode_ID = models.ForeignObject(Customer_salecode, on_delete=models.CASCADE,
                                                from_fields=['Customer_ID', 'Salecode_ID'], to_fields=['Customer_ID', 'Salecode_ID'])
    
    def __str__(self):
        return self.ID