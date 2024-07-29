from django.db import models

# Create your models here.
class musican(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    Instrument_type = models.CharField(max_length=30)
    
    def __str__(self):
        return self.First_Name
    
    