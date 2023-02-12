from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.core import serializers
from cart.models import Cart
from .models import Order

# Create your views here.
def orderTotal(request):
    template = loader.get_template('order_total.html')
    products = Cart.objects.filter(user=request.user)
    total = 0
    for product in products:
        total += product.quantity * product.product.price
    context = {
        "order_total": round(total, 2),
    }
    return HttpResponse(template.render(context, request))


def createOrder(request):
    json = serializers.serialize("json", Cart.objects.filter(user=request.user))
    Order.objects.create(user=request.user, json = json)
    Cart.objects.filter(user=request.user).delete()
    return redirect("/")


def allOrders(request):
    template = loader.get_template('all_orders.html')
    orders = Order.objects.filter(user=request.user)
    context = {
        "orders": orders,
    }
    return HttpResponse(template.render(context, request))