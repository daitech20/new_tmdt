from django.shortcuts import render
from users.api.serializers import (
    RegisterCustomerSerializer,
    CustomJWTSerializer,
    RegisterStaffSerializer,
    StaffUpdateSerializer,
    CustomerUpdateSerializer,
    Usererializer,
)
from users.models import User, Staff, Customer
from core.permissions import IsSuperUser, IsStaffUser, IsOwnerOrReadOnly
from rest_framework import generics, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
# Create your views here.

class RegisterCustomerView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterCustomerSerializer


class RegisterStaffView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterStaffSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class StaffUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff
    serializer_class = StaffUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsStaffUser, IsOwnerOrReadOnly]


class CustomerUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer
    serializer_class = CustomerUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerOrReadOnly]


class UserDetail(generics.RetrieveAPIView):
    queryset = User
    serializer_class = Usererializer
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated]