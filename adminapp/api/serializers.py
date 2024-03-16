from rest_framework import serializers
from adminapp.models import AdminProfile


class AdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields ='__all__'
        