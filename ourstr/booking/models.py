from django.db import models
from django.contrib.auth.models import User
from adm.models import Customer

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import timedelta
from adm.models import Product  # Importing Product from the adm app


def get_default_booking_end():
    return timezone.now() +timedelta(days=2)

class Booking(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_start = models.DateTimeField(default=timezone.now)
    booking_end = models.DateTimeField(default=get_default_booking_end)
    confirmed = models.BooleanField(default=False) 
    

    def save(self, *args, **kwargs):
        # Calculate total price based on product price and quantity
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)