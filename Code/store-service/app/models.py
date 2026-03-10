from django.db import models

# Create your models here.
class Store(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name