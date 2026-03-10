from django.db import models

# Create your models here.
class admin(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)

    def __str__(self):
        return self.name