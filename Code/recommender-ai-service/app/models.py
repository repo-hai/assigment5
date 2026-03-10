from django.db import models

# Create your models here.
class Recommender_AI_system(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    ModelName = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Layer = models.IntegerField()
    
    def __str__(self):
        return self.name