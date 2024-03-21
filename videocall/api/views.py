from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from videocall.models import *
from mentorapp.models import *
from rest_framework.response import Response

class VideocallView(APIView):
    def post(self,request):
        pass



 
