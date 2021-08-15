import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = "message"
        self.room_group_name = "newgroup"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name

        )
        self.accept()
        self.send(json.dumps("Connection accepted in webserver"))

    def receive(self,text_data):
        print(text_data)
        

    def disconnect(self,event):
        print(event)


    def get_data(self,event):
        print(event['value'])