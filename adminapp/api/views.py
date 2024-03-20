from django.http import HttpResponse
from django.shortcuts import render
from adminapp.models import *
from myapp.models import *
from mentorapp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from myapp.api.serializers import *
from mentorapp.api.serializers import *
from rest_framework_simplejwt.tokens import RefreshToken

class AdminLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        admin_obj = AdminProfile.objects.create(username=username,password=password)

        refresh = RefreshToken.for_user(admin_obj)
        serialized = AdminProfileSerializer(admin_obj)
        print(serialized.data,"nokkkkkk")

        return Response({
            'message': 'success',
            'userdataa': serialized.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    
    

        
class AdminprofileView(APIView):
    def get(self,request):
        userobjects = UserProfile.objects.all()
        if userobjects:
            serializer=UserProfileSerializer(userobjects,many=True)
            return Response({'message':'passed','userdata':serializer.data})
        
class MentorlistView(APIView):
    def get(self,request):
        mentorobj=MentorProfile.objects.all()
        if mentorobj:
            serializer=MentorProfileSerializer(mentorobj,many=True)
            return Response({'message':'passed','userdata':serializer.data}) 

class ClasslistView(APIView):
    def get(self,request):
        
        classobj=Class.objects.all()
        
        print (classobj,"all the datils for classmanagement")
        if classobj:
            serializer=ClassSerializer(classobj,many=True)
            return Response({'message':'passed','classdata':serializer.data}) 
        
class MentorApprovalView(APIView):
    def post(self, request):
        mentor_id = request.data.get('mentor_id')
        print(mentor_id,"...")
        is_approved = request.data.get('is_approved')
        print(is_approved,"STATUS")

        try:
            mentor_profile = MentorProfile.objects.get(id=mentor_id)
            mentor_profile.is_approved = is_approved
            mentor_profile.save()

            serializer = MentorProfileSerializer(mentor_profile)
            return Response({"message": "success", "mentor_data": serializer.data})
        except MentorProfile.DoesNotExist:
            return Response({"message": "Mentor not found"})
        

class EntrolledStudentsCourselisting(APIView):
    def get(self,request):
        order_obj=Order.objects.all()
        print(order_obj,"hiiiiiiii")
        serializer = OrderSerializer(order_obj, many=True)
        print(serializer.data)
        return Response({'success': True, 'userdata':serializer.data})


class ToggleBlockUnblockView(APIView):
    def patch(self, request, user_id):
        print(user_id,"user id vanno")
        user_profiles = UserProfile.objects.filter(id=user_id)

        if not user_profiles.exists():
            return Response({'success': False, 'error': 'User not found'})

        user_profile = user_profiles.first()
        user_profile.blocked = not user_profile.blocked
        user_profile.save()

        return Response({'success': True})

    

