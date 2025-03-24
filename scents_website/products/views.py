from django.shortcuts import render
from .models import Product  # Import your Product model

def product_view(request):
    products = Product.objects.all()

    # Check if products exist, otherwise use placeholders
    placeholder_list = [1, 2, 3, 4, 5, 6, 7, 8] if not products.exists() else []

    return render(request, "products/products.html", {
        "products": products,
        "placeholder_list": placeholder_list  # Pass placeholder list to template
    })

