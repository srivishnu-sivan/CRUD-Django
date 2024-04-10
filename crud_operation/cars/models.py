from django.db import models

# Create your models here.

class Cars(models.Model):
    car_name = models.CharField(max_length=255)
    car_version = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    car_price = models.IntegerField()
    
    def __str__(self):
        return "Car Name"
    
