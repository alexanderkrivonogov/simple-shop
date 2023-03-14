from django_filters.rest_framework import filters, FilterSet


class CategoryFilterSet(FilterSet):
    parent = filters.NumberFilter(field_name='parent')


class ProductFilterSet(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    category = filters.NumberFilter(field_name='category')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
