from django.db import models

# Create your models here.
class Rating(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Score = models.IntegerField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Book_ID = models.CharField(max_length=255)
    Customer_ID = models.CharField(max_length=255)

    def __str__(self):
        return f"Rating for Book ID {self.Book_ID}: {self.Score}"
    
class Comment(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Context = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Book_ID = models.CharField(max_length=255)
    Customer_ID = models.CharField(max_length=255)
    Staff_ID = models.CharField(max_length=255, null=True, blank=True)
    Comment_ID = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
            
    def __str__(self):
        return f"Comment for Book ID {self.Book_ID}: {self.Content[:50]}..."