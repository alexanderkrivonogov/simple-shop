from rest_framework import generics, mixins
from rest_framework.viewsets import GenericViewSet

from api.catalog.filters import CategoryFilterSet, ProductFilterSet
from api.catalog.serializers import CategorySerializer, ProductListSerializer, ProductRetrieveSerializer
from apps.catalog.models import Category, Product


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilterSet


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filterset_class = ProductFilterSet

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductRetrieveSerializer

        if self.action == 'list':
            return ProductListSerializer

        raise ValueError(f'Invalid action: {self.action}')

    def get_queryset(self):
        return super().get_queryset().filter(available=True, stock__gt=0)
