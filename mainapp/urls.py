from django.urls import path
from mainapp import views

urlpatterns = [
    path('getStocks/', views.getStocks),
    path('getStocksPrice/', views.getStocksPrice),
] 