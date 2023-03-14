from django.urls import path
from rest_framework.routers import DefaultRouter

from api.catalog import views

router = DefaultRouter()
router.register('product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('category/', views.CategoryListAPIView.as_view(), name='category'),
]
