from django . db import models

class Book(models.Model) :
    ID = models.CharField(max_length =255 , primary_key =True)
    Title = models.CharField(max_length =255)
    Author = models.CharField(max_length =255)
    Price = models.DecimalField(max_digits =10 , decimal_places =2)
    Stock = models.IntegerField()
    ISBN = models.CharField(max_length =255)
    Image_url = models.URLField(max_length =255)
    Weight = models.DecimalField(max_digits =10 , decimal_places =2)
    Dimensions = models.CharField(max_length =255)
    Amazon_url = models.URLField(max_length =255)
    RowID = models.CharField(max_length =255)
    BookSupplier_ID = models.CharField(max_length =255)

    def __str__(self) :
        return self.Title

