from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Stocks
import json

from django.http import JsonResponse

# Create your views here.
def home(request):
    context= Stocks.objects.values("symbol")
    return render(request,"home/home.html",{"stocks":context})

def profile(request):
    context= Stocks.objects.values("symbol")
    return render(request,"accounts/profile.html",{"stocks":context})