import json
import copy
from urllib.parse import parse_qs
from asyncio import tasks

from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import WebsocketConsumer
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from .models import StockDetail, Channel


class StockConsumer(WebsocketConsumer):

    @sync_to_async
    def addToCeleryBeat(self, stocks):
        task = PeriodicTask.objects.filter(name="every-10-seconds")
        if (len(task)) > 0:
            task = task.first()
            args = json.loads(task.args)
            args = args[0]
            for stock in stocks:
                if stock not in args:
                    args.append(stock)
            task.args = json.dumps([args])
            task.save()
        else:
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=10, period=IntervalSchedule.SECONDS)
            task = PeriodicTask.objects.create(
                interval=schedule, name='every-10-seconds', task="mainapp.tasks.update", args=json.dumps([stocks]))
    
    @sync_to_async
    def addToStockDetail(self, stocks):
        channel_name = self.channel_name
        channel, _ = Channel.objects.get_or_create(channel_name = channel_name)
        for stock in stocks:
            s, created = StockDetail.objects.get_or_create(stock = stock)
            s.channel.add(channel)


    def connect(self):
        print('[log] Got connection request!!')
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'stock_%s' % self.room_name

        print(self.room_group_name)
        print("[log] channel name : ", self.channel_name)
        
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        query_params = parse_qs(self.scope['query_string'].decode())
        print(query_params)
        stocks = query_params['stocks']
        print(stocks)

        # add to celery beat
        async_to_sync(self.addToCeleryBeat)(stocks)

        # add user to stockdetail
        async_to_sync(self.addToStockDetail)(stocks)

        return self.accept()
    
    @sync_to_async
    def helper_func(self):
        channel_name = self.channel_name
        channel = Channel.objects.get(channel_name = channel_name)
        stocks = StockDetail.objects.filter(channel = channel)
        task = PeriodicTask.objects.get(name="every-10-seconds")
        args = json.loads(task.args)
        args = args[0]
        for stock in stocks:
            stock.channel.remove(channel)
            if stock.channel.count() == 0:
                args.remove(stock.stock)
                stock.delete()
        
        channel.delete()
        
        if args == None:
            args = []
        
        if len(args) == 0:
            task.delete()
        else:
            task.args = json.dumps([args])
            task.save()

    def disconnect(self, close_code):
        print('[log] Got Disconnection request!!')

        # Reconfiguring tasks
        async_to_sync(self.helper_func)()

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'stocks_update',
                'message': message
            }
        )

    @sync_to_async
    def selectUserStocks(self):
        channel_name = self.channel_name
        try:
            channel = Channel.objects.get(channel_name = channel_name)
            user_stocks = channel.stockdetail_set.values_list('stock', flat = True)
            return list(user_stocks)
        except:
            print('[Log] Channel not found')
            return []

    # Receive message from room group
    def stocks_update(self, event):
        message = event['message']
        message = copy.copy(message)

        user_stocks = async_to_sync(self.selectUserStocks)()

        keys = message.keys()
        for key in list(keys):
            if key not in user_stocks:
                del message[key]
            
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
