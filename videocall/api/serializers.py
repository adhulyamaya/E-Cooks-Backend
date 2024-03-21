from rest_framework import serializers
from videocall.models import VideoCallSession
from mentorapp.api.serializers import OrderSerializer  # Import OrderSerializer

class VideoCallSessionSerializer(serializers.ModelSerializer):
    order = OrderSerializer() 
    
    class Meta:
        model = VideoCallSession
        fields = ['id', 'order', 'start_time', 'end_time', 'channel_name']

