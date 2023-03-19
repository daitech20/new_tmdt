from django.db import models
from users.models import User

# Create your models here.

class Keyword(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    keyword = models.ManyToManyField(Keyword, blank=True, related_name="brands_keyword")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    keyword = models.ManyToManyField(Keyword, blank=True, related_name="categories_keyword")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products_brand")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products_category")
    keyword = models.ManyToManyField(Keyword, blank=True, related_name="products_keyword")
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_user")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments_product")
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)