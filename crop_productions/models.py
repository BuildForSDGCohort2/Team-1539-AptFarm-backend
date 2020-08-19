from django.db import models
from procedures.models import *
# Create your models here.

class Crops(models.Model):
    name = models.CharField(max_length=50)
    procedures = models.ForeignKey(Procedures, on_delete=models.CASCADE)
    fertilizer = 


    def __str__(self):
        return self.name


