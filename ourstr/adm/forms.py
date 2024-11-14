import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import admin
from django.shortcuts import render, redirect
from django.utils.html import format_html
from .models import  Product
from django import forms
from django.core.exceptions import ValidationError




class InvoiceForm(forms.ModelForm):
    
    class Meta:
        model =  Product
        fields = ["name","brand","description","bulk_price","price","quantity",'category','supplier']

import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=10)
    register_no = forms.CharField(max_length=12)

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'register_no', 'password1', 'password2']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        # Ensure the phone number contains only digits
        if not phone_number.isdigit():
            raise ValidationError("Phone number must contain only digits.")
        
        # Ensure phone number is exactly 10 digits long
        if len(phone_number) != 10:
            raise ValidationError("Enter correct Phone number .")
        
        return phone_number

    def clean_register_no(self):
        register_no = self.cleaned_data.get('register_no')

        # Ensure the register_no is exactly 2 characters long
        if len(register_no) != 12:
            raise ValidationError("Check your Register number.")
        
        # Optionally, you can check if the first three characters are 'VDA' (as in your original validation)
        if not register_no.startswith('VDA'):
            raise ValidationError("Register number must start with 'VDA'.")
        
        return register_no

    # Custom password validation for password1 and password2
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        # Ensure the password is at least 8 characters long
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        # Check if the password contains at least one special character
        if not re.search(r'[\W_]', password1):  # \W matches any non-word character, including special characters
            raise ValidationError("Password must contain at least one special character.")
        
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')

        # Check if password2 matches password1 (default behavior of UserCreationForm)
        if password2 != self.cleaned_data.get('password1'):
            raise ValidationError("Passwords do not match.")
        
        # Ensure that password2 also contains a special character (as done in password1)
        if len(password2) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        
        if not re.search(r'[\W_]', password2):
            raise ValidationError("Password must contain at least one special character.")
        
        return password2





# class RegistrationForm(UserCreationForm):
#     phone_number=forms.CharField(max_length=15)
#     register_no=forms.CharField(max_length=88)

#     class Meta:
#         model = User
#         fields = ['username','phone_number','register_no','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# class SaleForm(forms.ModelForm):
#     class Meta:
#         model = Sale
#         fields = ['product', 'quantity_sold', 'customer_name', 'payment_method']

#     def clean_quantity_sold(self):
#         product = self.cleaned_data.get('product')
#         quantity_sold = self.cleaned_data.get('quantity_sold')

#         if product and quantity_sold > product.quantity:
#             raise forms.ValidationError(f'Insufficient stock. Available quantity: {product.quantity}')
#         return quantity_sold

    

      








# admin



# class SaleAdmin(admin.ModelAdmin):
#     list_display = ('customer_name', 'sell_date')
#     actions = ['sell_products']

#     def sell_products(self, request, queryset):
#         if 'apply' in request.POST:
#             customer_name = request.POST.get('customer_name')
#             sale = Sale.objects.create(customer_name=customer_name)
#             for product in queryset:
#                 quantity = int(request.POST.get(f'quantity_{product.id}', 0))
#                 if quantity > 0:
#                     SaleItem.objects.create(sale=sale, product=product, quantity_sold=quantity)
#                     product.quantity -= quantity  # Update product stock
#                     product.save()
#             self.message_user(request, "Sale completed successfully.")
#             return redirect('..')

#         # Inline HTML form
#         context = {
#             'products': queryset,
#         }

#         html = '''
#         <h1>Sell Products</h1>
#         <form method="post">
#             %s
#             <button type="submit" name="apply">Sell</button>
#         </form>
#         ''' % self.get_product_html(context['products'])

#         return render(request, 'admin/sell_products.html', {'html': html})

#     def get_product_html(self, products):
#         product_rows = []
#         for product in products:
#             product_rows.append(f'''
#             <tr>
#                 <td>{product.name}</td>
#                 <td><input type="number" name="quantity_{product.id}" min="0"></td>
#             </tr>
#             ''')
#         return f'''
#         <table>
#             <tr>
#                 <th>Product</th>
#                 <th>Quantity</th>
#             </tr>
#             {''.join(product_rows)}
#         </table>
#         <label for="customer_name">Customer Name:</label>
#         <input type="text" name="customer_name" required>
#         '''

#     sell_products.short_description = "Sell selected products"


