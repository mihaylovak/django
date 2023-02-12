from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Cart

# Create your views here.
def cart(request):
    template = loader.get_template('cart.html')
    products = Cart.objects.filter(user=request.user)
    if request.method == "POST":
        for product in products:
            if int(request.POST.get('cart_id', 0)) == product.id:
                product.quantity = int(request.POST.get('quantity', 1))
                product.save()
                break
    context = {
        "cart_products": products,
    }
    return HttpResponse(template.render(context, request))