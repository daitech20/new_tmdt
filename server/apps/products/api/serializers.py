from rest_framework import serializers
from products.models import (
    Brand,
    Category,
    Keyword,
    Product,
    Comment,
)
from drf_extra_fields.fields import Base64ImageField

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    keyword = KeywordSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandListSerializer(serializers.ModelSerializer):
    keyword = KeywordSerializer(many=True)
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    comments_product = CommentSerializer(many=True)


    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'image': {
                'required': False
            }
        }


class ProductListSerializer(serializers.ModelSerializer):
    keyword = KeywordSerializer(many=True)
    brand = BrandListSerializer()
    category = CategoryDetailerializer()

    class Meta:
        model = Product
        fields = '__all__'