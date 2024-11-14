# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import get_object_or_404, redirect
# from adm.models import Product
# from .models import Booking

# def book_item(request, product_id, quantity):
#     product = get_object_or_404(Product, id=product_id)

#     if product.quantity >= quantity:
#         # Reduce available stock
#         product.quantity -= quantity
#         product.reserved_quantity += quantity
#         product.save()

#         # Create a booking record
#         Booking.objects.create(
#             product=product,
#             quantity=quantity
#         )
#         return redirect('booking_success')  # Redirect to a success page or similar
#     else:
#         return redirect('out_of_stock_page')  # Redirect if not enough stock


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Booking
from adm.models import Product
from adm.models import Customer




# @login_required
# def create_booking(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     quantity = request.POST.get('quantity')
   
#     booking = Booking(
#         product=product,
#         quantity=quantity,
#         customer=request.user  # Set the logged-in user as the customer
#     )
#     booking.save()
#     return redirect('booking_page')  # Redirect to the booking page

# from .models import Booking
# from django.contrib.auth.decorators import login_required

# @login_required
# def booking_page(request):
#     # Get bookings for the current user that are not yet confirmed
#     customer=get_object_or_404(Customer,user=request.user)
#     bookings = Booking.objects.filter(customer=customer, confirmed=False)
#     total_price = sum(booking.total_price for booking in bookings)
   
#     return render(request, 'booking/booking_page.html', {'bookings': bookings, 'total_price': total_price})



# @csrf_exempt
def confirm_order(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id, customer=request.user)
        booking.confirmed = True
        booking.save()
        return JsonResponse({'status': 'success', 'message': 'Order confirmed successfully.'})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request'}, status=400)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
   
    # Get the cart from session
    cart = request.session.get('cart', [])
   
    # Get the quantity from the form (ensure it's a valid number)
    try:
        selected_quantity = int(request.POST.get('quantity', 1))
    except (ValueError, TypeError):
        messages.error(request, "Invalid quantity selected.")
        return redirect('product_list')  # Redirect back to product list if error

    if selected_quantity < 1:
        messages.error(request, "Quantity must be at least 1.")
        return redirect('product_list')  # Redirect back to product list

    # Check if the product is already in the cart
    current_cart_quantity = 0
    for item in cart:
        if item['id'] == product.id:
            current_cart_quantity = item['quantity']
            break
   
    # Total quantity (already in cart + new one being added)
    new_quantity = current_cart_quantity + selected_quantity

    if new_quantity > product.quantity:
        # If adding to cart exceeds available stock, show an error message
        messages.error(request, f'Cannot add more than {product.quantity} items of {product.name} to the cart.')
        return redirect('product_list')

    # Update the cart (either add new or update quantity if already in cart)
    item_found = False
    for item in cart:
        if item['id'] == product.id:
            item['quantity'] = new_quantity
            item_found = True
            break
    if not item_found:
        cart.append({
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'quantity': selected_quantity
        })
   
    # Save updated cart back to session
    request.session['cart'] = cart
   
    # Redirect to booking page
    return redirect('booking_page')

# def booking_page(request):
#     cart = request.session.get('cart', [])
#     return render(request, 'booking/booking_page.html', {'cart': cart})

# def booking_page(request):
#     cart = request.session.get('cart', [])
#     return render(request, 'booking/booking_page.html', {'cart': cart})

def booking_page(request):
    # Fetch cart from session, defaulting to an empty list if not found
    cart = request.session.get('cart', [])

    total_price = 0  # Initialize total price
    
    # Calculate total price while handling potential errors in cart items
    for item in cart:
        try:
            price = float(item.get('price', 0))  # Default price to 0 if not found
            quantity = int(item.get('quantity', 1))  # Default quantity to 1 if not found
            total_price += price * quantity
        except (ValueError, TypeError):
            continue  # Skip this item if there's an error
    
    # Round the total price to 2 decimal places for currency formatting
    total_price = round(total_price, 2)

    return render(request, 'booking/booking_page.html', {
        'cart': cart,
        'total_price': total_price,
    })

def remove_from_cart(request, product_id):
    # Get the cart from the session
    cart = request.session.get('cart', [])

    # Filter out the item to be removed by its product_id
    cart = [item for item in cart if item['id'] != product_id]

    # Update the session with the modified cart
    request.session['cart'] = cart

    # Optionally, you can show a success message
    # messages.success(request, 'Item removed from cart successfully.')

    # Redirect back to the booking page or cart page
    return redirect('booking_page') 