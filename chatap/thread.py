import threading
import time
from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync

class ThreadExample(threading.Thread):

    def run(self):
        try:
            print("thread has been executed")
            channel_layer= get_channel_layer()
            for i in range(0,10):
                async_to_sync(channel_layer.group_send)(
                    "newgroup",{
                        'type':'get_data',
                        'value': i
                    }
             
                )
                time.sleep(1)

        except Exception as e:
             print(e)
