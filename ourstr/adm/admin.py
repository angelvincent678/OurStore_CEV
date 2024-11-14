from django.contrib import admin
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.contrib.admin.models import LogEntry
from .models import Supplier,Category,Product,Customer
from .forms import InvoiceForm 



# Register your models here.
admin.site.register(LogEntry)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Customer)







# class SaleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'customer_name', 'payment_method', 'total_amount')
#     search_fields = ('customer_name', 'payment_method')

#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         form.base_fields['product'].queryset = Product.objects.filter(quantity__gt=0)
#         return form

#     class Media:
#         js = ('js/select_product.js',)  # custom JavaScript file
#         css = {'all': ('css/select_product.css',)}  # custom CSS file

# admin.site.unregister(Sale)
# admin.site.register(Sale, SaleAdmin)




# class SaleAdmin(admin.ModelAdmin):
#     list_display = ("id","product",'quantity_sold','customer_name','payment_method','per_price',"total_amount",'sell_date')

#     def save_model(self, request, obj, form, change):
#         if obj.quantity_sold > obj.product.quantity:
#             self.message_user(request, "Insufficient quantity available", level="error")
#         else:
#             obj.save()

# admin.site.register(Sale, SaleAdmin)



class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'bulk_price', 'price', 'quantity', 'updated_at')
    form=InvoiceForm
    list_filter=['name','brand','price','category']
    search_fields=['name','price']

admin.site.register(Product,InvoiceAdmin)













