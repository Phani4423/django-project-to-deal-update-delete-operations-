from django.shortcuts import render
from app.models import *

# Create your views here.
def display(request):
    return render(request,'display.html')
def table(request):
    pgs.objects.update_or_create(cost = 5000,defaults={'area':'nellore'})
    LPGS = pgs.objects.filter(cost__gt = 6000)
    d = {'LPGS': LPGS}
    return render(request,'table.html',d)
def tables(request):
    futurs.objects.all()
    LPGS = futurs.objects.all()
    d = {'LPGS': LPGS}
    return render(request,'tables.html',d)
def tables_update(request):
    #futurs.objects.filter(wifi = 3).update(food = 'yes')
    futurs.objects.filter(wifi = 3).update(food ='no')
    LPGS = futurs.objects.all().order_by('wifi')
    d = {'LPGS': LPGS}
    return render(request,'tables.html',d)
def tables(request):
    futurs.objects.filter(food = 'two tims').delete()
    LPGS = futurs.objects.all()
    d = {'LPGS': LPGS}
    return render(request,'tables.html',d)


