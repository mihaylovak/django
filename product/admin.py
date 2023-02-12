from django.contrib import admin
from .models import Product
# Register your models here.




class ProductAdmin(admin.ModelAdmin): # new
    readonly_fields = ['img_preview']

admin.site.register(Product, ProductAdmin)