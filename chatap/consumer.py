import json
from channels.generic.websocket import WebsocketConsumer
import time

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(json.dumps("Connection accepted in webserver"))

    def receive(self,text_data):
        print(text_data)
        

    def disconnect(self,*args,**kwargs):
        self.send(json.dumps("I am disconnecting from websocket"))
        self.disconnet()