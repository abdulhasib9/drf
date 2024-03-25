from django.db import models

# Create your models here.
class Cars(models.Model):
    brand = models.CharField(max_length=255)
    year = models.IntegerField()
    type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.brand
    