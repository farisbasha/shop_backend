
from rest_framework import serializers

from .models import Customer, Product, Category, Order, ProductTag, Review


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


#Product Tag Serializer
class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = '__all__'
        
#Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
#Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
