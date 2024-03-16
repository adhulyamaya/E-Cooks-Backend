from rest_framework import serializers
from mentorapp.models import MentorProfile,Class,Order


class MentorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfile
        fields ='__all__'

       
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields ='__all__'        


class OrderSerializer(serializers.ModelSerializer):
    booked_class = ClassSerializer()
    student_username = serializers.CharField(source='student.username', read_only=True)
    mentor_name = serializers.CharField(source='mentor.name', read_only=True)
    class_name=serializers.CharField(source='booked_class',read_only=True)
    class Meta:
        model = Order
        fields ='__all__'         