from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    # return HttpResponse("Home Page")
    
    # render data from database
    orders =  Order.objects.all()
    customers= Customer.objects.all()
    
    total_customers = customers.count()
    total_orders = orders.count()
    
    total_delivered = orders.filter(status='Delivered').count()
    total_pending = orders.filter(status='Pending').count()
    
    # container dictionaries for sending data to webpage
    
    container = {
        'orders':orders,
        'customers':customers,
        'total_customers':total_customers,
        'total_orders':total_orders,
        'total_delivered':total_delivered,
        'total_pending':total_pending
    }
    
    return render(request, 'CoffeeShop/dashboard.html', container)

def products(request):
    products = Product.objects.all()
    return render(request, 'CoffeeShop/products.html', {'products':products})

def customers(request):
    return render(request, 'CoffeeShop/customers.html')