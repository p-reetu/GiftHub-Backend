from django.shortcuts import render
from .serializers import GiftSerializer, UserRegistrationSerializer, UserLoginSerializer
from .models import Gift, CustUser
from rest_framework import status, response
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate
#from django.contrib.auth.models import User

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = CustUser.objects.all()
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return response.Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return response.Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
    
class GiftsView(ListCreateAPIView):
    serializer_class = GiftSerializer
    queryset = Gift.objects.all()