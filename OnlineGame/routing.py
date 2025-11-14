from django.urls import re_path
from OnlineGame.consumers import GameConsumer



websocket_urlpatterns = [
    re_path(r"ws/sala/(?P<codigo>\w+)/$", GameConsumer.as_asgi()),
]