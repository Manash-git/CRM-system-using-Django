from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .orderForm import createOrderFrom

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

def customers(request,pk):
    
    # queries from database
    customer= Customer.objects.get(id=pk)
    orders= customer.order_set.all()
    order_count = orders.count()
    
    container = {
        'customer':customer,
        'orders':orders,
        'order_count':order_count
    }
    
    return render(request, 'CoffeeShop/customers.html', container)

def createOrder(request):
    form = createOrderFrom()
    
    if request.method == 'POST':
        form = createOrderFrom(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')
    
    container = {'form':form}
    
    return render(request,'CoffeeShop/createOrder.html', container)