from django.contrib import admin

# Register your models here.

from .models import Customer, Product, Category, Order, Review, ProductTag

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)

admin.site.register(Review)
admin.site.register(ProductTag)
