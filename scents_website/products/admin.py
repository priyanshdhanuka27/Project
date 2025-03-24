from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')  # What to show in the admin list view
    search_fields = ('name',)  # Allow searching by product name
