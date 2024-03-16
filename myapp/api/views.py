from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *
from mentorapp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from mentorapp.api.serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
# from allauth.socialaccount.models import SocialAccount

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            userobj = UserProfile.objects.get(username=username, password=password)
            if userobj.blocked:
                return Response({"message": "error", "error": "User is blocked"})
        except UserProfile.DoesNotExist:
            return Response({"message": "error", "error": "Invalid credentials"})

        refresh = RefreshToken.for_user(userobj)
        serialized = UserProfileSerializer(userobj)
        return Response({
            "message": "success",
            "userdata": serialized.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })


class GoogleLoginView(APIView):
    def post(self, request):
        google_data = request.data.get('googleToken')
        print(google_data,"??????????????")
        google_user_id = google_data.get('sub')
        email = google_data.get('email')
        print(email,"??????????????")
        username=google_data.get('name')
        picture=google_data.get('picture')
        given_name=google_data.get("given_name")

        try:
            user_profile = UserProfile.objects.get(email=email)
            print(user_profile)
        except UserProfile.DoesNotExist:
            user_profile = UserProfile.objects.create(
                username=username,
                name=given_name,
                email=email,
                password='',  
                image=picture, 
            )
        print(user_profile,"YEAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

        if user_profile:
            refresh = RefreshToken.for_user(user_profile)
            serialized_data = UserProfileSerializer(user_profile)
            print(serialized_data.data,"ingalu katholeee")
            return Response({
                "message": "success", "userdata": serialized_data.data,"refresh": str(refresh),"access": str(refresh.access_token),
                })
        else:
            return Response({"message":"invalid credentials"})   
       

class SignupView(APIView):
    def post(self,request):
        username=request.data.get('username')
        name=request.data.get('name')
        email=request.data.get('email')
        phone=request.data.get('phone')
        # image=request.data.get('image')
        password=request.data.get('password')

        userobj = UserProfile.objects.create(username=username,name=name,email=email,
                                             phone=phone,password=password)
        print(userobj)
        return Response({"message":"success"})
    


class CourseListing(APIView):
    def get(self,request):
     courseobj=Class.objects.all() 
     if courseobj:
        serializer=ClassSerializer(courseobj,many=True)
        return Response({"message":"passedddddddddddddddddddddddddddd",'classdata':serializer.data})



class ImageuploadView(APIView):
    def post(self,request):
        print(request,"hi req")
        image = request.data.get('imageurl')
        id = request.data.get('id')
        # print(image,"image ahn ???????????????")
        userobj=UserProfile.objects.get(id=id)
        userobj.image=image
        userobj.save()

        serialized = UserProfileSerializer(userobj)
        return Response({"message":"image updated","details":serialized.data})
    
    


class CreateView(APIView):
    def post(self,request):
        username=request.data.get('username')
        name=request.data.get('name')
        email=request.data.get('email')
        phone=request.data.get('phone')
        image=request.data.get('image')
        password=request.data.get("password")

        print(username,name,".................")

        userobj=UserProfile.objects.create(username=username,name=name,email=email,phone=phone,image=image,password=password)
        print(userobj,"??////")
        serialized=UserProfileSerializer(userobj)
        return Response({"message":"success","data":serialized.data})
    


class GetEditView(APIView):
    def get(self,request,id):
        userobj=UserProfile.objects.get(id=id)

        serialized=UserProfileSerializer(userobj)
        return Response({"message":"success","data":serialized.data})


class EditingView(APIView):
    def post(self,request):
        id=request.data.get('id')
        username=request.data.get('username')
        name=request.data.get('name')
        email=request.data.get('email')
        phone=request.data.get('phone')
        image=request.data.get('image')
        password=request.data.get("password")

        userobj=UserProfile.objects.get(id=id)

        userobj.username=username
        userobj.name=name
        userobj.email=email
        userobj.phone=phone
        userobj.image=image
        userobj.password=password
        userobj.save()
        serialized =UserProfileSerializer(userobj)
        return Response({"message":"success","data":serialized.data})
    

class DeleteView(APIView):
    def post(self,request,id):
        try:
            userobj=UserProfile.objects.get(id=id)
            userobj.delete()
            return Response({"message":"success"})
        except:
            return Response({"message":"failed"})
        

class SearchView(APIView):
    def post(self,request):
        value=request.data.get("value")
        filtered_users=UserProfile.objects.filter(username__istartswith=value)
        filtered_users_serialized=UserProfileSerializer(filtered_users,many=True) 
        return Response({"message":"success","data":filtered_users_serialized.data})


class PurchasedCourseListing(APIView):
    def get(self,request):
        orderobj=Order.objects.all()
        print(orderobj,"ffffffffffffffffffff")
        if orderobj:
            serializer=OrderSerializer(orderobj,many=True)
            print(serializer.data,"..............")
            return Response({'message':'passed','userdata':serializer.data}) 
        

        return Response({"message":"failed"})
          
    






                
    

    


        
        
        

        






