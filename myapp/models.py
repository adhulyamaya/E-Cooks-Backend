from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=50,blank=False)
    name = models.CharField(max_length=50,blank=False)
    email = models.CharField(max_length=100,unique=True,blank=False)
    phone = models.PositiveIntegerField(blank=True, null=True)
    password = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.id}"

