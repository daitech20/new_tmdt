from rest_framework.permissions import IsAdminUser
from rest_framework import permissions
from users.models import User, Staff, Customer

class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
    

class IsStaffUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True
        customer = Customer.objects.filter(user=request.user)

        if customer:
            try:
                return obj.customer == customer
            except:
                pass
        
        return obj.user == request.user