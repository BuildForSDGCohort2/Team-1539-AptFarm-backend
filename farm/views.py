from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import Form
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import simplejson as json
from django.template.context_processors import csrf

import requests

# Create your views here.


def index(request):
    if request.method == 'POST':
        feeds_cost = int(request.POST['feeds_cost'])
        no_of_birds = int(request.POST['no_of_bird'])
        small_equipment = int(request.POST['small_equipment'])
        paid_labor = int(request.POST['paid_labor'])
        transportation = int(request.POST['transportation'])
        inKind_expenses  = int(request.POST['inKind_expenses'])
        


    
        a = inKind_expenses + paid_labor + small_equipment + transportation
        i =  7
        b = 25
        c = i/ b
        f = (feeds_cost * c) * no_of_birds
        r = f + a
        total = round(r,2)
        


        return render(request, 'index.html', {'result':total})
    else:

        return render(request, 'index.html')



def evaluate(request):
    
    return render(request, 'evaluate.html')

        


def project(request):
    return render(request, 'project.html')
  
        
    

def reminder(request):
    
   return render(request, 'reminder.html')
        
    

   

def accounts(request):
    
    
    return render(request, 'profile/index.html')
        
    

    


def profile(request):
   return render(request, 'profile/index.html')

       
    # If a user is logged in, redirect them to a page informing them of such

    

  

    





