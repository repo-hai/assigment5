from django.db import models

# Create your models here.
class Inventory(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Name = models.CharField(max_length=255)
    Total_quantity = models.IntegerField()
    Type = models.CharField(max_length=255)

    def __str__(self):
        return self.Name
    
class Shelf(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Name = models.CharField(max_length=255)
    Quantity = models.IntegerField()
    Type = models.CharField(max_length=255)
    Inventory_ID = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Row(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Name = models.CharField(max_length=255)
    Quantity = models.IntegerField()
    Type = models.CharField(max_length=255)
    Shelf_ID = models.ForeignKey(Shelf, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name