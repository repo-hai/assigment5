from django.db import models

# Create your models here.
class Inventory_staff(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)
    House_number = models.CharField(max_length=255)
    Street = models.CharField(max_length=255)
    District = models.CharField(max_length=255)
    Province = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Telephone = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    Telephone = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Receipt(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    Handle_at = models.DateTimeField(auto_now_add=True)
    Total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory_staff_ID = models.ForeignKey(Inventory_staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID    

class Book_supplier(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    Description = models.CharField(max_length=255)
    Receipt_ID = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    Supplier_ID = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    BookID = models.CharField(max_length=10)

    def __str__(self):
        return self.ID
    

