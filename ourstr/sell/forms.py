

from django import forms
from .models import  Sale



class SaleForm(forms.ModelForm):


  
    class Meta:
        model = Sale
        fields = ['product', 'quantity_sold', 'customer_name', 'payment_method']

    def clean_quantity_sold(self):
        product = self.cleaned_data.get('product')
        quantity_sold = self.cleaned_data.get('quantity_sold')

        if product and quantity_sold > product.quantity:
            raise forms.ValidationError(f'Insufficient stock. Available quantity: {product.quantity}')
        return quantity_sold

