from django.contrib import admin
from users.models import User, Staff, Customer
# Register your models here.

admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Customer)


