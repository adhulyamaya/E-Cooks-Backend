from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

  path('start-video-call/<int:mentor_id>/<int:student_id>/', VideocallView.as_view(), name='start_video_call'),
  # path('videochating/',VideocallView.as_view(),name="videochating"),
   
    ]
