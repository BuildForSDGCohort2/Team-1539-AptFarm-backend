from django.db import models
from chickens.models import Chicken
# Create your models here.
class Layers(models.Model):
    chicken = models.ForeignKey(Chicken, on_delete=models.CASCADE)