from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from products.models import Product, ProductCategory, Basket
from users.models import User
# Create your views here.

# функции = контроллеры = фьюхи

def index(request):
    context = {
        'title': 'Makiell Store',
    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None, page_number=1):
    # PRODUCTS = Product.objects.all()
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    
    # categories = ProductCategory.objects.all()
    # non_zero_categories = []
    # for category in categories:
    #     for product in PRODUCTS:
    #         if product.category.name == category.name:
    #             non_zero_categories.append(category)
    #             break
        
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator
    }
    return render(request, 'products/products.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])