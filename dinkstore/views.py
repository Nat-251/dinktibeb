from django.shortcuts import render
from .models import * 

# create your view here. 

def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'dinkstore/store.html', context)

def cart(request):
	context = {}
	return render(request, 'dinkstore/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'dinkstore/checkout.html', context)
