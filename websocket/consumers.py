import json
from channels.generic.websocket import AsyncWebsocketConsumer
from jwt import decode as jwt_decode
from urllib.parse import parse_qs
from django.conf import settings

import time

# Use Database Functions
from database.views import insert_communication_data
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
    #     self.room_name = self.scope['url_route']['kwargs']['room_name']
    #     self.room_group_name = 'chat_%s' % self.room_name

    #     # Join room group
    #     await self.channel_layer.group_add(
    #         self.room_group_name,
    #         self.channel_name
    #     )

    #     await self.accept()

    # async def disconnect(self, close_code):
    #     # Leave room group
    #     await self.channel_layer.group_discard(
    #         self.room_group_name,
    #         self.channel_name
    #     )
        self.token = parse_qs(self.scope["query_string"].decode("utf8"))["token"][0]
        decoded_jwt = jwt_decode(self.token,settings.CHAT_SECRET_KEY,algorithms=["HS256"])
        rooms = decoded_jwt['rooms']
        print(rooms, 'line 33')
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
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        message_detail = json.loads(text_data)
        print(message_detail, 'line 30')
        message_detail['message_data'][0].update({'timestamp':time.time()})
        
        # Change Plain_Text Message into Hex
        message_detail['message_data'][0]['message'] = message_detail['message_data'][0]['message'].encode().hex()
    #     payload = {'msg_status': 'SUCCESS', 'color': '#2ecc71', 'output': 'Message Sent Successfully', 'message_data': [{
	# 	'room_type': contact_details['room_type'],
	# 	'room': contact_details['room'],
	# 	'sender': ethereum.selectedAddress.toUpperCase(),
	# 	'receiver': contact_details['rcvr_wallet_addresses'],
	# 	'message': message,
    #   'timestamp': timestamp,
	# }]}
    
        insertion_status = insert_communication_data(message_detail['message_data'][0])
        if insertion_status['msg_status']=='FAILED':
            message_detail.update(insertion_status)

        print(message_detail, message_detail['message_data'], 'line28')

        # # Here Code will be updated which will let us insert new communication datas in the communication_data Database


        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'msg_detail': message_detail
            }
        )
        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {'msg_detail':message_detail}
        # )

    # Receive message from room group
    async def chat_message(self, event):
        # message = event['message']
        message_detail = event['msg_detail']
        print(message_detail, 'line74')
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message_detail
        }))