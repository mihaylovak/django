from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Product
from cart.models import Cart

# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return HttpResponse(template.render(context, request))


def addProductToCart(request, id):
    if not request.user.is_authenticated:
        return redirect("/login/")
    # return HttpResponse(f"Product {id} added to cart")
    template = loader.get_template('addProductToCart.html')
    product = Product.objects.get(id=id)
    already_exists = True
    print(product)
    print(Cart.objects.filter(product=product))
    if not Cart.objects.filter(product=id, user=request.user).exists():
        already_exists = False
        cart = Cart(product=product, user=request.user)
        cart.save()
    else:
        already_exists = True
        cart = Cart.objects.filter(product=id)[0]
    context = {
        "product": product,
        "product_cart_id": cart.id,
        "already_exists": already_exists,
    }
    return HttpResponse(template.render(context, request))

def removeProductFromCart(request, id):
    Cart.objects.filter(id=id, user=request.user).delete()
    return redirect("/cart/")