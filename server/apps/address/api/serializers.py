from rest_framework import serializers
from address.models import (
    Wards,
    Provinces,
    Districts,
    AddressUser,
    DeliveryAddress
)
from users.models import (
    Staff,
    Customer,
)


class ProvincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinces
        fields = '__all__'


class DistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'


class WardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wards
        fields = '__all__'


class AddressUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = model = AddressUser
        fields = (
            "specific",
            "ward",
        )

    def create(self, validated_data):
        user = self.context['request'].user
        address_user = AddressUser.objects.none()
        
        address_user_exist = AddressUser.objects.filter(user=user).first()

        if address_user_exist:
            raise serializers.ValidationError({"result": "address user exists!"})
        
        address_user = AddressUser.objects.create(
            specific=validated_data['specific'],
            ward=validated_data['ward'],
            user=user,
        )
        address_user.save()

        return address_user

class AddressUserUpdateSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField("get_address")

    class Meta:
        model = AddressUser
        fields = (
            "id",
            "specific",
            "ward",
            "address",
        )

    def get_address(self, obj):
        return f'{obj.specific}, {obj.ward.full_name} {obj.ward.district_code.full_name}, {obj.ward.district_code.province_code.full_name}'


class DeliveryAddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = model = DeliveryAddress
        fields = (
            "specific",
            "ward",
            "phone",
            "recipient_first_name",
            "recipient_last_name"
        )

    def create(self, validated_data):
        user = self.context['request'].user
        customer = Customer.objects.filter(user=user).first()
        if customer is None:
            raise serializers.ValidationError({"result": "you are not customer!"})
        
        delivery_address = DeliveryAddress.objects.create(
            specific=validated_data['specific'],
            phone=validated_data['phone'],
            ward=validated_data['ward'],
            customer=customer,
            recipient_first_name=validated_data['recipient_first_name'],
            recipient_last_name=validated_data['recipient_last_name'],
        )
        delivery_address.save()

        return delivery_address


class DeliveryAddressListSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField("get_address")

    class Meta:
        model = DeliveryAddress
        fields = (
            "id",
            "specific",
            "ward",
            "phone",
            "is_default",
            "recipient_last_name",
            "recipient_first_name",
            "address",
        )

    def get_address(self, obj):
        return f'{obj.specific}, {obj.ward.full_name} {obj.ward.district_code.full_name}, {obj.ward.district_code.province_code.full_name}'
