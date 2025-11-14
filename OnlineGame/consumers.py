# OnlineGame/OnlineGame/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Tomamos el código de la sala desde la URL
        self.room_name = self.scope['url_route']['kwargs']['codigo']
        self.room_group_name = f"game_{self.room_name}"

        # Unir al grupo
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({
            "message": f"Conectado a la sala {self.room_name}"
        }))

    async def disconnect(self, close_code):
        # Salir del grupo al desconectar
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")

        # Reenviar el mensaje a todos los miembros de la sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "game_action",
                "action": action
            }
        )

    # Este método se llama cuando se envía un mensaje al grupo
    async def game_action(self, event):
        action = event['action']

        # Enviar al cliente
        await self.send(text_data=json.dumps({
            "message": f"Recibido: {action}"
        }))
