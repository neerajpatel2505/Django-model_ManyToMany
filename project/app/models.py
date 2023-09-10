from django.db import models

# Create your models here.

class FuelTypeModel(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=255)
    fueltype = models.ManyToManyField(FuelTypeModel)
    def __str__(self):
        return self.name