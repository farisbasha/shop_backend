from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    image = models.ImageField(upload_to="profile_pics")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="category_pics")

    def __str__(self):
        return self.name
    
class Product(models.Model):

    name = models.CharField(max_length=200)
    seller = models.ForeignKey(Customer,on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    description = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    
    image = models.ImageField(upload_to="product_pics")
    def __str__(self):
        return self.name
    

class ProductTag(models.Model):
    class TagType(models.TextChoices):
        NEW = 'NEW'
        HOT = 'HOT'
        SALE = 'SALE'
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    tag = models.CharField(max_length=200,choices=TagType.choices)
    
    def __str__(self):
        return self.product.name + " is " + self.tag
    
class Review(models.Model):
    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    review = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=Rating.choices)
    
    def __str__(self):
        return self.customer.name + " reviewed " + self.product.name
    

    
class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = 'PENDING'
        DELIVERED = 'DELIVERED'
        CANCELLED = 'CANCELLED'
    
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,choices=OrderStatus.choices,default=OrderStatus.PENDING)
    def __str__(self):
        return self.customer.name + " ordered " + self.product.name