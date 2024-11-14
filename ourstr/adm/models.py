from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=10)
    register_no=models.CharField(max_length=88,unique=True)

    def __str__(self): 
        return self.user.username

class Supplier(models.Model):
    name=models.CharField(max_length=88)
    contact=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#define category  model

class Category (models.Model):
    name=models.CharField(max_length=88)
    description=models.TextField()

    def __str__(self):
        return self.name

#define product model
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    brand=models.CharField(max_length=100)
    description=models.TextField()
    bulk_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()
    updated_at=models.DateTimeField(auto_now=True)
    # reserved_quantity = models.PositiveIntegerField(default=0)  # Number of items currently reserved

    @property
    def available_quantity(self):
        return self.quantity  # Shows real-time stock available for new purchases or bookings

    def __str__(self):
        return f"{self.name}-- ₹{self.price} ----- {self.brand} ---> {self.description[:50]}-----{self.quantity}stock"

        
         
      

    def display_details(self):
         return f" {self.brand}    :::  {self.description[:50]}"










        



    


    



        


    
    

