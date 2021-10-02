from django.shortcuts import render

from shop_product.models import Product
from shop_category.models import Category


def header(request):
    categories = Category.objects.filter(is_sub=False)
    context = {
        'categories': categories
    }
    return render(request, 'shared/_Header.html', context)


def footer(request):
    context = {}
    return render(request, 'shared/_Footer.html', context)


def home_page(request):
    product = Product.objects.all()

    context = {
        'product': product,

    }
    return render(request, 'home_page.html', context)