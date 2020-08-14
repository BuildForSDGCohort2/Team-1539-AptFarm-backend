from django.db import models
from django.apps import apps
from broiler.models import Broiler
from chickens.models import Chicken
# Create your models here.




class Cost(models.Model):
    feeds_cost = models.DecimalField(max_digits=10,decimal_places=3, null=True)
    no_of_birds = models.IntegerField()
    small_equipment = models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    paid_labor = models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    transportation = models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    inKind_expenses  = models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    


    def Tota_cost(self):
        a = self.inKind_expenses + self.paid_labor + self.small_equipment + self.transportation
        i =  7
        b = 25
        c = i / b
        f = (self.feeds_cost * c) / b
        ff = self.no_of_birds * f
        total = ff + a
        return total






        

    