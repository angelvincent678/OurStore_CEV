from django.db import models
from django.db.models import Sum, F, ExpressionWrapper, DecimalField, Value
from django.db.models.functions import TruncDate, Coalesce
from adm.models import Product

class SaleManager(models.Manager):
    def daily_total_transactions(self):
        return (
            self.get_queryset()
            .annotate(date=TruncDate('sell_date'))
            .values('date')
            .annotate(
                daily_total=Sum(
                    ExpressionWrapper(
                        Coalesce(F('product_price'), Value(0)) * F('quantity_sold'),
                        output_field=DecimalField()
                    )
                ),
                daily_wholesale_total=Sum(
                    ExpressionWrapper(
                        Coalesce(F('bulk_price'), Value(0)) * F('quantity_sold'),
                        output_field=DecimalField()
                    )
                ),
            )
            .order_by('date')
        )

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    sell_date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=55)
    payment_method = models.CharField(max_length=55)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bulk_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    objects = SaleManager()

    def save(self, *args, **kwargs):
        if not self.product_price:
            self.product_price = self.product.price
        if not self.bulk_price:
            self.bulk_price = self.product.bulk_price
        self.product.quantity -= self.quantity_sold
        self.product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name}"


