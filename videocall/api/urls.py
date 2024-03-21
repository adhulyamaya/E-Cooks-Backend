from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path('videochating/',VideocallView.as_view(),name="videochating"),
   
    ]
