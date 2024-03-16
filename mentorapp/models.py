from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from myapp.models import UserProfile
from notification.models import Notification




class MentorProfile(models.Model):
    name = models.CharField(max_length=255,blank=False,default="")
    fullname=models.CharField(max_length=255,blank=False,default="")
    bio = models.TextField(max_length=500,blank=False,default="")
    email = models.EmailField(max_length=255, unique=True,default="")
    expertise = models.CharField(max_length=255,blank=False,default="")
    experience = models.TextField(max_length=200,default="",null=True)
    age=models.IntegerField(default=23)
    image = models.ImageField(max_length=500, default="", null=True, blank=True)
    address = models.CharField(max_length=250, blank=True, null=True, default="")
    certificate = models.FileField(max_length=500, default="", null=True, blank=True)
    password = models.CharField(max_length=50)       
    is_approved = models.BooleanField(default=False)
    availability_start_time = models.TimeField(null=True, blank=True)
    availability_end_time = models.TimeField(null=True, blank=True)
   
    def __str__(self):
        return f"{self.name} {self.id}"


    
class Class(models.Model):
    mentor = models.ForeignKey(MentorProfile, on_delete=models.CASCADE, related_name='courses')
    class_name = models.CharField(max_length=255, blank=False)
    course_description = models.TextField(max_length=500, blank=False)
    syllabus = models.TextField(max_length=500,default="Default Syllabus")
    date = models.DateField(null=True, blank=True)
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    thumbnail = models.CharField(max_length=500, default="")
    schedule = models.CharField(max_length=255,null=True, blank=True)   
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.class_name

class Order(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    mentor = models.ForeignKey(MentorProfile, on_delete=models.CASCADE ,null=True, blank=True)
    booked_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50)
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2)
    booking_date = models.DateField(null=True, blank=True)
    booking_time = models.TimeField(null=True, blank=True)
    booking_ampm = models.CharField(max_length=2, null=True, blank=True) 
    confirmation_status = models.BooleanField(default=False)


    def __str__(self):
        return f"Order ID: {self.pk}"
    
    
