from django.contrib import admin
from address.models import AddressUser, DeliveryAddress
# Register your models here.

admin.site.register(AddressUser)
admin.site.register(DeliveryAddress)

