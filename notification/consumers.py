import json
from channels.generic.websocket import AsyncWebsocketConsumer
from myapp.models import UserProfile
from notification.models import Notification
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connected")
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print("WebSocket disconnected")
        await self.channel_layer.group_discard("notifications", self.channel_name)

    @database_sync_to_async
    def get_user_profile(self, user_id):
        return UserProfile.objects.get(pk=user_id)

    @database_sync_to_async
    def create_notification(self, recipient, content):
        return Notification.objects.create(recipient=recipient, content=content)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            recipient_id = data.get('recipient_id')
            content = data.get('content')

            if recipient_id is not None and content is not None:
                recipient = await self.get_user_profile(recipient_id)
                notification = await self.create_notification(recipient, content)

                recipient_data = {'id': recipient.id, 'username': recipient.username}
                notification_data = {
                    'id': notification.id,
                    'content': notification.content,
                    'timestamp': str(notification.timestamp),
                }

                # Send the notification to the recipient's channel group
                channel_layer = get_channel_layer()
                await channel_layer.group_send(
                    "notifications",  # Name of the channel group
                    {
                        'type': 'send_notification',  # Event type aanu 
                        'recipient': recipient_data,
                        'notification': notification_data,
                    }
                )
                print("Notification sent")
            else:
                print("Invalid message format: 'recipient_id' or 'content' is missing.")
        except json.JSONDecodeError:
            print("Invalid JSON format in the received data.")
        except Exception as e:
            print(f"Error during sending notification: {e}")

    async def send_notification(self, event):
        recipient = event['recipient']
        notification = event['notification']
        await self.send(text_data=json.dumps({
            'recipient': recipient,
            "notification": notification,
        }))

















# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from myapp.models import UserProfile
# from notification.models import Notification
# from channels.db import database_sync_to_async

# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         if 'user' in self.scope:
#             user = self.scope['user']
#             if user.isAuthenticated:
#                 user_id = str(user.id)
#                 self.room_group_name = f'notifications_{user_id}'
#                 await self.channel_layer.group_add(
#                     self.room_group_name,
#                     self.channel_name
#                 )
#                 await self.accept()
#             else:
#                 await self.close()
#         else:
#             await self.close()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#         await self.close(close_code)

#     @database_sync_to_async
#     def get_user_profile(self, user_id):
#         return UserProfile.objects.get(pk=user_id)

#     @database_sync_to_async
#     def create_notification(self, recipient, content):
#         return Notification.objects.create(recipient=recipient, content=content)

#     async def receive(self, text_data):
#         try:
#             data = json.loads(text_data)
#             recipient_id = data.get('recipient_id')
#             content = data.get('content')

#             if recipient_id is not None and content is not None:
#                 recipient = await self.get_user_profile(recipient_id)
#                 notification = await self.create_notification(recipient, content)

#                 recipient_data = {'id': recipient.id, 'username': recipient.username}
#                 notification_data = {
#                     'id': notification.id,
#                     'content': notification.content,
#                     'timestamp': str(notification.timestamp),
#                 }

#                 # Sending the notification to the recipient's WebSocket and channel group
#                 await self.send(text_data=json.dumps({
#                     'type': 'notification',
#                     'recipient': recipient_data,
#                     'notification': notification_data,
#                 }))

#                 # Sending the notification to the recipient's channel group
#                 await self.channel_layer.group_send(
#                     self.room_group_name,
#                     {
#                         'type': 'notification.message',
#                         'content': notification_data,
#                     }
#                 )
#             else:
#                 print("Invalid message format: 'recipient_id' or 'content' is missing.")
#         except json.JSONDecodeError:
#             print("Invalid JSON format in the received data.")
#         except Exception as e:
#             print(f"Error during sending: {e}")

#     async def notification_message(self, event):
#         content = event['content']
#         await self.send(text_data=json.dumps({
#             'type': 'notification',
#             'notification': content,
#         }))
