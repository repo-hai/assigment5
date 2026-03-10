from django.db import models

# Create your models here.
class Chatbox(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Customer_ID = models.CharField(max_length=255)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ID
    
class Client_support_staff(models.Model):
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
        return self.ID

class Message(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Chatbox_ID = models.CharField(max_length=255)
    Context = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Message_ID = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    Client_support_staff_ID = models.ForeignKey(Client_support_staff, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.ID