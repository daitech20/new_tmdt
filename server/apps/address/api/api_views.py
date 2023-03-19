from rest_framework import permissions
from rest_framework import generics, status
from address.models import (
    AddressUser,
    DeliveryAddress,
    Wards,
    Districts,
    Provinces
)
from users.models import(
    Customer
)
    
from address.api.serializers import (
    AddressUserCreateSerializer,
    AddressUserUpdateSerializer,
    WardsSerializer,
    DistrictsSerializer,
    ProvincesSerializer,
    DeliveryAddressCreateSerializer,
    DeliveryAddressListSerializer
)
from core.permissions import (
    IsOwnerOrReadOnly,
    IsSuperUser,
    IsStaffUser
)


class WardsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wards
    serializer_class = WardsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'code'


class WardsList(generics.ListAPIView):
    queryset = Wards
    serializer_class = WardsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'district_code'

    def get_queryset(self):
        district_code = self.kwargs['district_code']
        return Wards.objects.filter(district_code=district_code)


class DistrictsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Districts
    serializer_class = DistrictsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'code'


class DistrictsList(generics.ListAPIView):
    queryset = Districts
    serializer_class = DistrictsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'province_code'

    def get_queryset(self):
        province_code = self.kwargs['province_code']
        return Districts.objects.filter(province_code=province_code)


class ProvincesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provinces
    serializer_class = ProvincesSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'code'


class ProvincesList(generics.ListAPIView):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressUserCreate(generics.CreateAPIView):
    queryset = AddressUser
    serializer_class = AddressUserCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressUserUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddressUser
    serializer_class = AddressUserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'id'


class DeliveryAddressCreate(generics.CreateAPIView):
    queryset = DeliveryAddress
    serializer_class = DeliveryAddressCreateSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class DeliveryAddressUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryAddress
    serializer_class = DeliveryAddressListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'id'


class DeliveryAddressList(generics.ListAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        customer = Customer.objects.filter(user=user).first()
        if customer is not None:
            return DeliveryAddress.objects.filter(customer=customer)

        return DeliveryAddress.objects.all()
