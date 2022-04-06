from urllib import request
from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict={
        'product1':'Mac',
        'product2':'Iphone',
        'product3':'Samsung'
    }
    return render(request, 'productApp/products.html', product_dict)

# Create your views here.
def toys(request):
    product_dict={
        'product1':'Remote_Car',
        'product2':'Drone',
        'product3':'Rocket_Launcher'
    }
    return render(request, 'productApp/products.html', product_dict)

# Create your views here.
def shoes(request):
    product_dict={
        'product1':'Nike',
        'product2':'Adidas',
        'product3':'Shoopen'
    }
    return render(request, 'productApp/products.html', product_dict)

def index(request):
    return render(request, 'productApp/index.html')