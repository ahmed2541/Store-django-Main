
from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    Email = models.EmailField(max_length=254)
    location = models.CharField(max_length=70)

    
    def __str__(self):
        return self.email