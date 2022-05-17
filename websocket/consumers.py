import json
from channels.generic.websocket import AsyncWebsocketConsumer
from jwt import decode as jwt_decode
from urllib.parse import parse_qs
from django.conf import settings

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.token = parse_qs(self.scope["query_string"].decode("utf8"))["token"][0]
        decoded_jwt = jwt_decode(self.token,settings.SECRET_KEY,algorithms=["HS256"])
        rooms = decoded_jwt['rooms']
        if rooms:
            for i in rooms:
                self.room_name = i
                self.room_group_name = 'chat_%s' % self.room_name

                # Join room group
                await self.channel_layer.group_add(
                    self.room_group_name,
                    self.channel_name
                )

            await self.accept()
        else:
            self.send(text_data=json.dumps({
                'message':'Unauthorized'
            }))

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))