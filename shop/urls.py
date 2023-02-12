"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import settings
from login.views import login, register, logout
from cart.views import cart
from orders.views import orderTotal, createOrder, allOrders
from product.views import home, addProductToCart, removeProductFromCart

urlpatterns = [
    path("", home),
    path("login/", login),
    path("logout/", logout),
    path("register/", register),
    path('admin/', admin.site.urls),
    path('addProductToCart/', home),
    path('allOrders/', allOrders),
    path('orderTotal/', orderTotal),
    path('createOrder/', createOrder),
    path('cart/', cart),
    path('addProductToCart/<int:id>/', addProductToCart),
    path('removeProductFromCart/<int:id>/', removeProductFromCart),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)