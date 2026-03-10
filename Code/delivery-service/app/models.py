from django.db import models

# Create your models here.
class Deliveryman(models.Model):
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
    
class Shipping(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Method = models.CharField(max_length=255)
    Fee = models.FloatField()
    Address = models.CharField(max_length=255)
    Phone_number = models.CharField(max_length=255)
    Created_at = models.DateTimeField(auto_now_add=True)
    Order_ID = models.CharField(max_length=255)

    def __str__(self):
        return self.ID

class Shipping_track(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Status = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Time = models.DateTimeField(auto_now_add=True)
    Shipping_ID = models.CharField(max_length=255)

    def __str__(self):
        return self.ID

class Shipping_delivery(models.Model):
    pk = models.CompositePrimaryKey('Shipping_ID', 'Deliveryman_ID')
    Shipping_ID = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    Deliveryman_ID = models.ForeignKey(Deliveryman, on_delete=models.CASCADE)
    Start_location = models.CharField(max_length=255)
    End_location = models.CharField(max_length=255)
    Start_time = models.DateTimeField(auto_now_add=True)
    End_time = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.ID