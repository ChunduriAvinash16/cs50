from django.shortcuts import render
import datetime
from django.http import HttpResponse
from time import gmtime, strftime
from django import forms

# Create your views here.
class Contact(forms.Form):
    yourname=forms.CharField()

def index(request):
    now=datetime.datetime.now()
    return render(request,'newyear/index.html',{
        "newyear":now.month==1 and now.day==1,
        "time":strftime("%A, %d %B %Y %H:%M:%S %Z", gmtime())
    })