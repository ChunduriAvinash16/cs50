from django.shortcuts import render
import datetime
from django.http import HttpResponse
from time import gmtime, strftime

# Create your views here.
def index(request):
    now=datetime.datetime.now()
    return render(request,'newyear/index.html',{
        "newyear":now.month==1 and now.day==1,
        "time":strftime("%A, %d %B %Y %H:%M:%S %Z", gmtime())
    })