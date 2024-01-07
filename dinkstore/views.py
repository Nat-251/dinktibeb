from django.shortcuts import render

def store(request):
     context = {}
     return render(request, 'dinkstore/store.html', context)

def cart(request):
     context = {}
     return render(request, 'dinkstore/cart.html', context)

def checkout(request):
      context = {}
      return render(request, 'dinkstore/checkout.html', context)
