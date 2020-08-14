from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import Form
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
        total = f + a
        


        return render(request, 'index.html', {'result':total})
    else:

        return render(request, 'index.html')



    


