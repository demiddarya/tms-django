from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from shop.models import Product, Category


# Create your views here.


def index(request: HttpResponse):
    products = Product.objects.all
    context = {'products_list': products}
    return render(request, 'shop/index.html', context)


def detail_product(request, product_id: int):
    information_of_product = get_object_or_404(Product, id=product_id)
    context = {'information_of_product': information_of_product}
    return render(request, "internet_shop/list_of_product.html", context)


def detail_category(request, category_id: int):
    info_category = get_object_or_404(Category, id=category_id)
    return render(request, 'shop/detail_category.html', {'info_category': info_category})
