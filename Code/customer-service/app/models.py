from django.db import models

# Create your models here.
class Customer(models.Model):
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
        return self.Name
    
class behavior(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Action = models.CharField(max_length=255)
    Handle_at = models.DateTimeField(auto_now_add=True)
    Counter = models.IntegerField(default=0)
    Customer_ID = models.CharField(max_length=255)
    Book_ID = models.CharField(max_length=255)

    def __str__(self):
        return self.ID

