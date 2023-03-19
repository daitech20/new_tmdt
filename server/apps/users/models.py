from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    """
    for authentication instead of usernames.
    """
    def create_user(self, username=None, password=None, is_staff=False, is_superuser=False):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True
        
        )
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, username=None, password=None):
        user = self.create_user(
            username=username,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save(using=self._db)

        return user


class User(AbstractUser):
    email = None
    first_name = None
    last_name = None

    objects = UserManager()

    def __str__(self):
        return self.username


class Staff(models.Model):
    avatar = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff_user")
    date_of_birth = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50, null=True, blank=True)


class Customer(models.Model):
    avatar = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_user")
    date_of_birth = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50, null=True, blank=True)