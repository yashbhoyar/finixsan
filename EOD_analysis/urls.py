from django.urls import path
from . import views 

urlpatterns=[
    path("",views.top_gainers_losers,name="EOD_analysis"),
    path("scanner/",views.EOD_screening,name="EOD_scanner"),
   
]

