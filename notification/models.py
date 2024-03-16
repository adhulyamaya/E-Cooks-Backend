from django.db import models
from myapp.models import UserProfile
from django.contrib.contenttypes.fields import GenericRelation

class Notification(models.Model):
    recipient  = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)  
    content = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
   

    def __str__(self):
        return f"Notification ID: {self.pk}, Content: {self.content}"
