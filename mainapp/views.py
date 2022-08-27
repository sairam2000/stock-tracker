from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from yahoo_fin.stock_info import tickers_nifty50, get_quote_table, get_live_price, get_quote_data

from threading import Thread
from queue import Queue

@api_view(['GET'])
def getStocks(request):
    stocks = tickers_nifty50()
    return Response({'stocks': stocks}, status=status.HTTP_200_OK)

@api_view(['POST'])
def getStocksPrice(request):
    stocks = request.data.get('stocks',[])
    available_stocks = tickers_nifty50()

    for stock in stocks:
        if stock not in available_stocks:
            return Response({'err':'Some Stocks are not listed in Nifty 50'}, status=status.HTTP_400_BAD_REQUEST)
    
    n_threads = len(stocks)
    thread_list = []
    results_queue = Queue()
    data = {}

    for i in range(n_threads):
        thread = Thread(target= lambda que,stock: que.put({stock: get_quote_data(stock)}), args=(results_queue, stocks[i]))
        thread_list.append(thread)
        thread_list[i].start()
    
    for thread in thread_list:
        thread.join()

    while not results_queue.empty():
        result = results_queue.get()
        data.update(result)

    return Response({'stockPrices': data}, status=status.HTTP_200_OK)
