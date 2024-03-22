from django.db import models

from mentorapp.models import Order

class VideoCallSession(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    channel_name = models.CharField(max_length=255, default='video_call_{uuid.uuid4().hex}')
  
    def __str__(self):
       return f'Video call session Id: {self.pk}, for Order ID: {self.order.pk}'



