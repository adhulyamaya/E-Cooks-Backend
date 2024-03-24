import json
from chat.models import ChatMessage
from myapp.models import UserProfile
from mentorapp.models import MentorProfile
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'chat_room'
        self.room_group_name = f'chat_{self.room_name}'

        #  room group lekk join
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            # Parse the received JSON data
            text_data_json = json.loads(text_data)
            print(text_data,"rext")
            message = text_data_json['message']
            print(message,"message")
            sender_type = text_data_json['sender_type']
            print(sender_type,"rext")
            sender_id = text_data_json['sender_id']
            receiver_type = text_data_json['receiver_type']
            receiver_id = text_data_json['receiver_id']
        except json.JSONDecodeError:
            await self.send_error_message("Invalid JSON format")
            return
        except KeyError as e:
            await self.send_error_message(f"Missing key in JSON data: {e}")
            return

       
        await self.save_message_to_database(message, sender_type, sender_id, receiver_type, receiver_id)

        # room group ilekk msg snd
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_type': sender_type,
                'sender_id': sender_id,
                'receiver_type': receiver_type,
                'receiver_id': receiver_id,
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

    @sync_to_async
    def save_message_to_database(self, message, sender_type, sender_id, receiver_type, receiver_id):
        try:
            # Check if the sender and receiver exist
            sender_profile = UserProfile.objects.get(id=sender_id)
            receiver_profile = MentorProfile.objects.get(id=receiver_id)
        except :
          
            return
        ChatMessage.objects.create(
            sender_type=sender_type,
            sender=sender_profile,
            receiver_type=receiver_type,
            receiver=receiver_profile,
            message=message
        )

        print(ChatMessage,"hllllllllllllllllllllllllllllllll")

    async def send_error_message(self, error_message):
        await self.send(text_data=json.dumps({
            'error': error_message
        }))





