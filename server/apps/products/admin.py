from django.contrib import admin
from products.models import Category, Brand, Keyword, Product, Comment
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Keyword)
admin.site.register(Comment)
