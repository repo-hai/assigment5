from django.db import models

# Create your models here.
class Payment(models.Model):
    ID = models.CharField(max_length=36, primary_key=True)  # UUID as string
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.CharField(max_length=20)
    Created_at = models.DateTimeField(auto_now_add=True)
    Method_name = models.CharField(max_length=20)
    Currency = models.CharField(max_length=10)
    Order_ID = models.CharField(max_length=36)

    def __str__(self):
        return f"Payment {self.id}: {self.amount} {self.currency} - {self.status}"