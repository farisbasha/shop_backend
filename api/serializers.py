
from rest_framework import serializers

from .models import Customer, Product, Category, Order

#Customer Serializer Login
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer

        exclude = ('password',)
    



#Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    seller = CustomerSerializer()
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

#Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

#Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
