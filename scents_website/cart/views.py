from django.shortcuts import render, redirect
from .models import Product, CartItem  # Assuming you have a Product and CartItem model
from django.contrib.auth.decorators import login_required

# This view handles the cart page for both authenticated and unauthenticated users
def cart_view(request):
    if request.user.is_authenticated:
        # For authenticated users, retrieve cart items from the CartItem model
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.get_total_price() for item in cart_items)
        return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})
    else:
        # For unauthenticated users, retrieve cart items from session
        cart = request.session.get('cart', [])
        cart_items = []
        total_price = 0

        for item in cart:
            product = Product.objects.get(id=item['product_id'])
            cart_items.append({
                'name': product.name,
                'price': product.price,
                'quantity': item['quantity'],
            })
            total_price += product.price * item['quantity']

        return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

# This view handles adding items to the cart (for both authenticated and unauthenticated users)
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    # For authenticated users, you would add to CartItem model
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
        cart_item.save()
    else:
        # For unauthenticated users, we use session-based cart
        cart = request.session.get('cart', [])
        
        # Check if the product is already in the session cart
        existing_item = next((item for item in cart if item['product_id'] == product.id), None)
        
        if existing_item:
            existing_item['quantity'] += 1
        else:
            cart.append({
                'product_id': product.id,
                'name': product.name,
                'price': product.price,
                'quantity': 1,
            })
        
        # Save the cart back to session
        request.session['cart'] = cart
    
    return redirect('cart')

# Example of handling cart removal (for authenticated users)
@login_required
def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        CartItem.objects.filter(user=request.user, product_id=product_id).delete()
        return redirect('cart')

from django.shortcuts import render
from .models import CartItem  # Make sure CartItem model is correctly imported

def cart_view(request):
    # Retrieve the cart data from the session
    cart = request.session.get('cart', [])
    cart_items = []
    total_price = 0

    for item in cart:
        # Assuming product_id exists in cart items
        product = Product.objects.get(id=item['product_id'])  
        item_total = product.price * item['quantity']
        cart_items.append({
            'name': product.name,
            'price': product.price,
            'quantity': item['quantity'],
            'total': item_total
        })
        total_price += item_total
    
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

from django.shortcuts import render
from .models import Product

def cart_view(request):
    cart = request.session.get('cart', [])
    cart_items = []
    total_price = 0

    # Loop through cart items and fetch product details
    for item in cart:
        product = Product.objects.get(id=item['product_id'])  # Assuming the cart stores product IDs
        item_total = product.price * item['quantity']  # Calculate total for each item
        cart_items.append({
            'name': product.name,
            'price': product.price,
            'quantity': item['quantity'],
            'total': item_total
        })
        total_price += item_total  # Add to overall total

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})
# views.py

from django.http import JsonResponse
from django.shortcuts import redirect
from .models import CartItem

def update_cart_item(request, item_id, action):
    if request.method == 'POST':
        cart_item = CartItem.objects.get(id=item_id)
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def remove_from_cart(request, item_id):
    if request.method == 'POST':
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
