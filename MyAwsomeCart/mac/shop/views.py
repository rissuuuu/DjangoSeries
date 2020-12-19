from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product
from math import ceil
def index(request):
    products=Product.objects.all()

    n=len(products)
    nslides=n//4+ ceil((n/4)-(n//4))
    # params={'no_of_slides':nslides,'range':range(1+nslides),'product':products}
    allproducts=[[products,range(1+nslides),nslides],
                 [products,range(1+nslides),nslides],
                 [products, range(1 + nslides), nslides],
                 [products, range(1 + nslides), nslides]
                 ]
    params={'allprods':allproducts}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def checkout(request):
    return HttpResponse("We are at checkout")

def prodview(request):
    return HttpResponse("We are at prodview")

def basic(request):
    return render(request,'shop/basic.html')





