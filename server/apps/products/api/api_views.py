from django.shortcuts import render
from rest_framework import filters
from products.api.serializers import (
    KeywordSerializer,
    CategoryListSerializer,
    CategoryDetailerializer,
    BrandListSerializer,
    BrandDetailerializer,
    ProductSerializer,
    ProductListSerializer,
    CommentSerializer
)
from products.models import (
    Product,
    Keyword,
    Brand,
    Category,
    Comment,
)
from core.permissions import IsSuperUser, IsStaffUser, IsOwnerOrReadOnly
from rest_framework import generics, status
from rest_framework import permissions
# Create your views here.


class KeywordList(generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    permission_classes = [permissions.IsAuthenticated]


class KeywordCreate(generics.CreateAPIView):
    queryset = Keyword
    serializer_class = KeywordSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]


class KeywordUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Keyword
    serializer_class = KeywordSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    lookup_field = 'id'


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = [permissions.IsAuthenticated]


class BrandDetail(generics.RetrieveAPIView):
    queryset = Brand
    serializer_class = BrandDetailerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class BrandCreate(generics.CreateAPIView):
    queryset = Brand
    serializer_class = BrandDetailerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]


class BrandUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand
    serializer_class = BrandDetailerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    lookup_field = 'id'


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category
    serializer_class = CategoryDetailerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class CategoryCreate(generics.CreateAPIView):
    queryset = Category
    serializer_class = CategoryDetailerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]


class CategoryUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category
    serializer_class = CategoryDetailerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    lookup_field = 'id'


class ProductCreate(generics.CreateAPIView):
    queryset = Product
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'keyword__name', 'category__name', 'brand__name']


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer
    lookup_field = 'id'


class CommentCreate(generics.CreateAPIView):
    queryset = Comment
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)