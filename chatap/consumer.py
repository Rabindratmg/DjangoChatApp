import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(json.dumps({"data":"Hi how are you?"}))

    def receive(self,text_data):
        print(text_data)

    def disconnect(self,*args,**kwargs):
        pass