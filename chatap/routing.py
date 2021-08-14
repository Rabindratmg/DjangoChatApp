
from django.urls import path
from . consumer import ChatConsumer


websocket_urlpatterns=[
    path('chat/',ChatConsumer.as_asgi()),


]
