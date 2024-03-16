# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from notification.models import Notification
# from .serializers import NotificationSerializer
# from mentorapp.models import Order
# from django.http import JsonResponse
# from notification.consumers import NotificationConsumer
# import json


# class Notifications(APIView):
#     def post(self, request):
#         order_id = request.get('order_id') 
#         enrolled_students = get_enrolled_students(order_id)

#         for student in enrolled_students:
#             send_notification(student.id, 'Your mentor confirmed the class time.')

#         return JsonResponse({'status': 'success'})

# def get_enrolled_students(order_id):
#     try:
#         order = Order.objects.get(pk=order_id)
#         return [order.student]
#     except Order.DoesNotExist:
#         return []

# def send_notification(user_id, message):
#     NotificationConsumer.send_notification(user_id, json.dumps({'content': message}))