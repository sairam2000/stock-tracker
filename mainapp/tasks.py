from threading import Thread
from queue import Queue
import simplejson as json

from celery import shared_task
from yahoo_fin.stock_info import tickers_nifty50, get_quote_data
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@shared_task(bind=True)
def update(self, stocks):
    available_stocks = tickers_nifty50()

    for stock in stocks:
        if stock not in available_stocks:
            stocks.remove(stock)

    n_threads = len(stocks)
    thread_list = []
    results_queue = Queue()
    data = {}

    for i in range(n_threads):
        thread = Thread(target=lambda que, stock: que.put({stock: json.loads(json.dumps(
            get_quote_data(stock), ignore_nan=True))}), args=(results_queue, stocks[i]))
        thread_list.append(thread)
        thread_list[i].start()

    for thread in thread_list:
        thread.join()

    while not results_queue.empty():
        result = results_queue.get()
        data.update(result)

    # sending data to group
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)("stock_track", {
        'type': 'stocks_update',
        'message': data
    })

    return 'success'
