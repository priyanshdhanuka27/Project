from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_view, name='products'),  # Change index to product_view
]
