from django.shortcuts import render
from .models import Product

def products(request):
	products = Product.objects.all()
	ctx = {'products':products}
	return render(request, 'products/products.html', ctx)
