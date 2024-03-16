from django.db import models

class AdminProfile(models.Model):
    username = models.CharField(max_length=50,blank=False)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username} {self.id}"