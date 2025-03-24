from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import settings here
from django.conf.urls.static import static  # Import static here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('about/', include('about.urls')),
    path('products/', include('products.urls')),
    path('login/', include('client_login.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
]

# Ensure media files are served in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
