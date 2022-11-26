from django.shortcuts import render
from nsetools import Nse
from .import screener
import json
import pandas as pd

# Create your views here.
def top_gainers_losers(request):
    nse=Nse()

    top_gainers=nse.get_top_gainers()
    top_losers=nse.get_top_losers()

    context={
        "top_gainers":top_gainers,
        "top_losers":top_losers
    }

    return render(request,"EOD_analysis/index.html",context)

def EOD_screening(request):
    
    buy_stocks=screener.EOD_buy(request)
    json_records1 =  buy_stocks.to_json(orient ='records') 
    buy_stocks = json.loads(json_records1) 

    sell_stocks=screener.sell_EOD(request)
    json_records2 =  sell_stocks.to_json(orient ='records') 
    sell_stocks = json.loads(json_records2)

    context = {
        'sell_stocks': sell_stocks ,
        'buy_stocks': buy_stocks 
    } 
    
    return render(request,"EOD_analysis/EOD_strategies.html",context)

