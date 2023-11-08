from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product

class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def product_list(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'product_list.html', {'products': products})
