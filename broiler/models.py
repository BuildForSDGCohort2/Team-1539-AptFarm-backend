from django.db import models
from procedures.models import *





class Broiler(models.Model):
    specie = models.CharField(max_length=50,null=True)
    procedures =models.ForeignKey(Procedures,on_delete=models.CASCADE,null=True)
    drugs =models.ManyToManyField(Drugs,null=True)
    vaccine = models.ManyToManyField(Vaccine,null=True)
    feed = models.ManyToManyField(Feed,null=True)

    
    def __str__(self):
        return self.specie
