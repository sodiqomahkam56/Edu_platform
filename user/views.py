from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView

from user.serializers import UserRegisterSerializer


# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
