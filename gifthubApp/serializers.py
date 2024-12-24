from .models import Gift, CustUser
from rest_framework import serializers
#from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustUser
        fields = ['username', 'password', 'email','age','gender']
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password:
            user = CustUser(**validated_data)
            user.set_password(password)  # This will hash the password
            user.save()
            return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ["sender","receiver","title","description",'image']