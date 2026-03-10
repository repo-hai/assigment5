from django.db import models

# Create your models here.
class Order(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Total_amount = models.FloatField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Address = models.CharField(max_length=255)
    Phone_number = models.CharField(max_length=20)
    Customer_ID = models.CharField(max_length=255)

    def __str__(self):
        return self.ID
    