from rest_framework import serializers
from apps.catalog.models import Product, Category, ProductPhoto


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'available', 'category', 'price', 'stock', 'banner']


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['photo']


class ProductRetrieveSerializer(serializers.ModelSerializer):
    photos = ProductPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'available', 'category', 'price', 'description', 'stock', 'photos', 'banner']
