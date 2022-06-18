from django.shortcuts import render

# Create your views here.

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer, UpdateSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    print(request.user.id)
    # user = User.objects.get(id=request.user.id)
    user = User.objects.all()
    print(user)
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


#Class based view to update user
class UpdateUserAPI(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = UpdateSerializer