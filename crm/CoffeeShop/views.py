from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("Home Page")
    return render(request, 'CoffeeShop/dashboard.html')

def products(request):
    return render(request, 'CoffeeShop/products.html')

def customers(request):
    return render(request, 'CoffeeShop/customers.html')