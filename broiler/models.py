from django.db import models
from django.apps import apps
from chickens.models import Chicken




# Create your models here.
class Broiler(models.Model):
    chicken = models.ForeignKey(Chicken, on_delete=models.CASCADE)

    



