#from django.http import response
from datetime import datetime
from django.shortcuts import render, HttpResponse
from home.models import Product
from math import ceil
# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    
    n = len(products)
    nsides =  n//4 + ceil((n/4)- n//4) 
    params = {'noof-side':nsides,'ranges':range(nsides),  'product':products}

    return render(request,'basic.html', params)

def about(request):
    context ={
        "varable1":"harry is great",

    }
    return render(request,'index.html',context)
def contact(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        category = request.POST.get("category")
        subcategory = request.POST.get("subcategory")
        desc = request.POST.get("desc")
        price = request.POST.get("price")
        product = Product(product_name=product_name,category=category,subcategory=subcategory,desc=desc,price=price,pub_date = datetime.today())
        product.save()
          

    return HttpResponse('/basic.html')