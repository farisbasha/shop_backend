from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Customer, Product, Category, Order
from .serializers import CustomerSerializer, ProductSerializer, CategorySerializer, OrderSerializer
# Create your views here.

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class CustomerLoginAPIView(generics.GenericAPIView):
    serializer_class = CustomerSerializer
    
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        try:
            customer = Customer.objects.get(email=email)
            if customer.password == password:
                data = CustomerSerializer(customer).data

                return Response(data,status=status.HTTP_200_OK)
            else:
                return Response({"message":"Invalid Credentials"},status=status.HTTP_404_NOT_FOUND)
        except Customer.DoesNotExist:
            return Response({"message":"Invalid Credentials"},status=status.HTTP_404_NOT_FOUND)