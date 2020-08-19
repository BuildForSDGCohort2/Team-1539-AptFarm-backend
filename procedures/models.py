from django.db import models

# Create your models here.



class Procedures(models.Model):
    title = models.CharField(max_length=50)
    overview = models.CharField(max_length=250)
    daily_activities = models.CharField(max_length=250)
    weekly_activities = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    application_date = models.CharField(max_length=50)
    dosage = models.CharField(max_length=50)



   # animal =
   
    def __str__(self):
        return self.name
    

class Drugs(models.Model):
    name = models.CharField(max_length=50)
    application_date = models.CharField(max_length=50)
    dosage = models.CharField(max_length=50)
  

    # animal =
   
    def __str__(self):
        return self.name

class Feed(models.Model):
    name = models.CharField(max_length=50)
    feeding_period = models.DurationField()
    #animal = 


    def __str__(self):
        return self.name



class Chemical(models.Model):
    name = models.CharField(max_length=50)
    application_time = models.DurationField()
    #animal = 


    def __str__(self):
        return self.name



class Fertilizer(models.Model):
    name = models.CharField(max_length=50)
    application_time = models.DurationField()
    #animal = 


    def __str__(self):
        return self.name

        

class AnimalDiseases(models.Model):
    name = models.CharField(max_length=50)
    vaccine = models.ManyToManyField(Vaccine,null=True)
    drugs = models.ManyToManyField(Drugs)
    control = models.TextField(max_length=250)

    def __str__(self):
        return self.name


