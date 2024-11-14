
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.db.models import Sum, F
from django.db.models.functions import TruncDate
from django.urls import path
from .models import Sale
from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse

class SaleAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'product_display',
        'bulk_price',
        'quantity_sold',
        'product_price',
        'total_amount',
        'payment_method',
        'sell_date',
          # Add total_amount to the list_display
    )

    def sell_date_display(self, obj):
        """Display sell_date in local time"""
        # Convert the datetime to the local system time
        return timezone.localtime(obj.sell_date).strftime('%Y-%m-%d %H:%M:%S')

    sell_date_display.short_description = 'Sell Date (Local Time)'


    def product_display(self, obj):
        """Display detailed product information."""
        return obj.product.display_details()
    product_display.short_description = 'Product'

    def total_amount(self, obj):
        """Calculate total amount (quantity_sold * product_price)."""
        return obj.quantity_sold * obj.product_price if obj.product_price else 0
    total_amount.short_description = 'Total Amount'  # Optional, defines the column header

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('chart-data/', self.admin_site.admin_view(self.chart_data), name='chart-data'),
        ]
        return custom_urls + urls

    def chart_data(self, request):
        """Returns JSON data for charts."""
        last_seven_days = timezone.now() - timedelta(days=7)
        recent_sales = Sale.objects.filter(sell_date__gte=last_seven_days)

        sold_products = recent_sales.values('product__name').annotate(total_sold=Sum('quantity_sold'))
        daily_data = (
            recent_sales
            .annotate(date=TruncDate('sell_date'))
            .values('date')
            .annotate(
                total_amount=Sum(F('product_price') * F('quantity_sold')),
                total_profit=Sum(F('product_price') * F('quantity_sold') - F('bulk_price') * F('quantity_sold'))
            )
            .order_by('date')
        )

        return JsonResponse({
            'sold_products': list(sold_products),
            'daily_data': list(daily_data),
        })

    def changelist_view(self, request, extra_context=None):
        """Custom changelist_view to show profit totals for the last 7 days."""
        last_seven_days = timezone.now() - timedelta(days=7)

        recent_sales = Sale.objects.filter(sell_date__gte=last_seven_days)

        daily_totals = (
            recent_sales
            .annotate(date=TruncDate('sell_date'))
            .values('date')
            .annotate(
                total_sales=Sum(F('product_price') * F('quantity_sold')),
                total_wholesale=Sum(F('bulk_price') * F('quantity_sold')),
                total_profit=Sum(F('product_price') * F('quantity_sold')) - Sum(F('bulk_price') * F('quantity_sold'))
            )
            .order_by('-date')  # Change to descending order
        )

        day_totals_list = [
            mark_safe(
                f"<hr style='border: 3px solid black;'>"
                f"<span style='font-size: 16px;'>Total sales amount for {daily_total['date']} = ₹{daily_total['total_sales'] or 0} <br>"
                f"Profit for the day = ₹{daily_total['total_profit'] or 0} "
                f"(Wholesale amount = ₹{daily_total['total_wholesale'] or 0})</span><br><br>"
                f"<hr style='border: 2px solid black;'>"
            )
            for daily_total in daily_totals
        ]

        extra_context = extra_context or {}
        extra_context['day_totals'] = day_totals_list
        extra_context['last_7_days_message'] = mark_safe("<span style='font-size: 20px; font-weight: bold;'>Last 7 days sales totals:</span>")
        return super().changelist_view(request, extra_context=extra_context)

    class Media:
        js = ('sell/js/sale_auto_price.js',)

# Register the Sale model with the customized SaleAdmin
admin.site.register(Sale, SaleAdmin)





