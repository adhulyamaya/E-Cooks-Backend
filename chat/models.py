from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ChatMessage(models.Model):
    sender_type = models.CharField(max_length=10, choices=(('user', 'User'), ('mentor', 'Mentor')))
    sender = models.ForeignKey(
        'myapp.UserProfile',  
        on_delete=models.CASCADE,
        related_name='sent_messages',
        null=True, blank=True
    )
    receiver_type = models.CharField(max_length=10, choices=(('user', 'User'), ('mentor', 'Mentor')))
    receiver = models.ForeignKey(
        'mentorapp.MentorProfile', 
        on_delete=models.CASCADE,
        related_name='received_messages',
        null=True, blank=True
    )
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        sender_name = self.get_sender_name()
        receiver_name = self.get_receiver_name()
        return f"From: {sender_name} To: {receiver_name} - {self.timestamp}"

    def get_sender_name(self):
        if self.sender_type == 'user':
            return self.sender.name if self.sender else "Unknown User"
        elif self.sender_type == 'mentor':
            return self.sender.fullname if self.sender else "Unknown Mentor"
        return "Unknown"

    def get_receiver_name(self):
        if self.receiver_type == 'user':
            return self.receiver.name if self.receiver else "Unknown User"
        elif self.receiver_type == 'mentor':
            return self.receiver.fullname if self.receiver else "Unknown Mentor"
        return "Unknown"






