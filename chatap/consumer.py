import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = "message"
        self.room_group_name = "newgroup"

        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name

        )
        await self.accept()
        await self.send(json.dumps("Connection accepted in webserver"))

    async def receive(self,text_data):
       print(text_data)
       await self.send(text_data)
        

    async def disconnect(self,event):
        await self.close()
        print(event)


    async def get_data(self,event):
        await self.send(json.dumps(event['value']))