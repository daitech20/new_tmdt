from rest_framework import serializers
from users.models import User, Customer, Staff
import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from apps.profiles.models import Profile


class RegisterCustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2',]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match"})
        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=attrs['password'])
            # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return attrs
    
    def create(self, validated_data):
        if User.objects.filter(username=validated_data["username"]).exists():
            raise serializers.ValidationError({"username": "username already exists"})
        
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        user.save()

        Customer.objects.create(user=user)

        return user


class RegisterStaffSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2',]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match"})
        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=attrs['password'])
            # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return attrs
    
    def create(self, validated_data):
        if User.objects.filter(username=validated_data["username"]).exists():
            raise serializers.ValidationError({"username": "username already exists"})
        
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_staff=True,
        )
        user.save()

        Staff.objects.create(user=user)

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({
                        'user':
                            {
                                'id': self.user.id,
                                'username': self.user.username,
                                'is_superuser': self.user.is_superuser,
                                'is_staff': self.user.is_staff,
                            },
                     })
        
        if self.user.is_staff and self.user.is_superuser == False:
            staff = Staff.objects.get(user=self.user)
            data.update({
                        'profile':
                            {
                                'id': staff.id,
                                'first_name': staff.first_name,
                                'last_name': staff.last_name,
                                'phone': staff.phone,
                                'email': staff.email
                            },
                     })
        
        if self.user.is_staff == False and self.user.is_superuser == False:
            customer = Customer.objects.get(user=self.user)
            data.update({
                        'profile':
                            {
                                'id': customer.id,
                                'first_name': customer.first_name,
                                'last_name': customer.last_name,
                                'phone': customer.phone,
                                'email': customer.email
                            },
                     })

        # and everything else you want to send in the response
        return data


class CustomJWTSerializer(MyTokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }
        # This is answering the original question, but do whatever you need here.
        # For example in my case I had to check a different model that stores more user info
        # But in the end, you should obtain the username to continue.
        user_obj = User.objects.filter(username=attrs.get("username")).first()
        if user_obj:
            credentials['username'] = user_obj.username

        return super().validate(credentials)


class StaffUpdateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Staff
        fields = '__all__'


class CustomerUpdateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Customer
        fields = '__all__'


class Usererializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']