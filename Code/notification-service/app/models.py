from django.db import models

# Create your models here.
class Notificaton(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Context = models.TextField()
    Type = models.CharField(max_length=255)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ID
    
class User_notification(models.Model):
    pk = models.CompositePrimaryKey('User_ID', 'Notification_ID')
    User_ID = models.CharField(max_length=255)
    Notification_ID = models.ForeignKey(Notificaton, on_delete=models.CASCADE)
    Status = models.IntegerField(default=0)  # 0: Unread, 1: Read

    def __str__(self):
        return f"{self.User_ID} - {self.Notification_ID}"