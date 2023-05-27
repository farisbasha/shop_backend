
from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView, CategoryListCreateAPIView, CategoryDetailAPIView, OrderListCreateAPIView, OrderDetailAPIView, CustomerLoginAPIView, HotProductListAPIView, NewProductListAPIView, SaleProductListAPIView

urlpatterns = [
    path('products/',ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/',ProductDetailAPIView.as_view()),
    path('products/hot/',HotProductListAPIView.as_view()),
    path('products/new/',NewProductListAPIView.as_view()),
    path('products/sale/',SaleProductListAPIView.as_view()),
    path('categories/',CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/',CategoryDetailAPIView.as_view()),
    path('orders/',OrderListCreateAPIView.as_view()),
    path('orders/<int:pk>/',OrderDetailAPIView.as_view()),
    path('login/',CustomerLoginAPIView.as_view()),
]