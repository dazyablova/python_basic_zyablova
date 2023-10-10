from django.shortcuts import render
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def product_list(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'product_list.html', {'products': products})
