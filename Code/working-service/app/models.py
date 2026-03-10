from django.db import models

# Create your models here.
class User(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=20)

    def __str__(self):
        return str(self.ID)

class Address(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    House_number = models.CharField(max_length=255)
    Street = models.CharField(max_length=255)
    District = models.CharField(max_length=255)
    Province = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Telephone = models.CharField(max_length=255)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ID)

class Shift(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    Type = models.CharField(max_length=20)
    Start = models.DateTimeField(auto_now_add=True)
    End = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.ID)
    
class Registration(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)
    Note = models.CharField(max_length=255)
    Status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.ID)
    
class Registration_Shift(models.Model):
    pk = models.CompositePrimaryKey('Registration_ID', 'Shift_ID')
    Registration_ID = models.ForeignKey(Registration, on_delete=models.CASCADE)
    Shift_ID = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ID)
    
class OfficialWorkingShift(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    Description = models.CharField(max_length=100)
    Handle_at = models.DateTimeField(auto_now_add=True)
    Registration_ID = models.CharField(max_length=10)
    Shift_ID = models.CharField(max_length=10)
    Registration_Shift_ID = models.ForeignObject(Registration_Shift, on_delete=models.CASCADE,
                                                from_fields=['Registration_ID', 'Shift_ID'], to_fields=['Registration_ID', 'Shift_ID'])

    def __str__(self):
        return str(self.ID)
    
class RecordWorking(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    Start_time = models.DateTimeField(auto_now_add=True)
    End_time = models.DateTimeField(auto_now_add=True)
    OfficialWorkingShift_ID = models.ForeignKey(OfficialWorkingShift, on_delete=models.CASCADE)
    SalaryReceipt_ID = models.ForeignKey('SalaryReceipt', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ID)

class SalaryReceipt(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Total_amount = models.FloatField()
    Currency = models.CharField(max_length=10)

    def __str__(self):
        return str(self.ID)