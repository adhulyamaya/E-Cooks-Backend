from django.contrib import admin

# Register your models here.


from django.contrib import admin
from mentorapp.models import *

admin.site.register(MentorProfile)
admin.site.register(Class )



admin.site.register(Order)