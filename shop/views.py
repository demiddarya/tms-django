from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserRegistrationForm, UserEditForm
from shop.models import Product, Category, OrderStatus, Order


def products(request: HttpResponse):
    context = {'products_list': Product.objects.all}
    return render(request, 'shop/products.html', context)


def detail_product(request, product_id: int):
    info_product = get_object_or_404(Product, id=product_id)
    context = {'info_product': info_product}
    return render(request, "shop/detail_product.html", context)


def detail_category(request, category_id: int):
    info_category = get_object_or_404(Category, id=category_id)
    return render(request, 'shop/detail_category.html', {'info_category': info_category})


def add_to_cart(request):
    assert request.method == 'POST'
    product_id = request.POST['product_id']
    if not request.user.is_authenticated:
        product_url = reverse('shop:detail_product', args=[product_id])
        redirect_url = reverse('login') + '?next=' + product_url
        return HttpResponseRedirect(redirect_url)
    product = get_object_or_404(Product, id=product_id)
    request.user.profile.ensure_shopping_cart().add_product(product)
    return redirect('shop:detail_product', product_id)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'shop/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'shop/register.html', {'user_form': user_form})


@login_required
def shopping_cart(request):
    request.user.profile.ensure_shopping_cart()
    return render(request, 'shop/shopping_cart.html')


@login_required
def submit_order(request):
    profile = request.user.profile
    order = profile.shopping_cart
    order.status = OrderStatus.COMPLETED
    order.save()
    profile.shopping_cart = Order.objects.create(profile=profile)
    profile.save()
    return render(request, 'shop/order_confirmed.html', {'order': order})


@login_required
def profile_info(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'shop/profile.html', {'user': user})


@login_required
def edit_profile(request, user_id):
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = get_object_or_404(User, id=user_id)
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('shop:profile', user.id)
    else:
        form = UserEditForm()
    return render(request, 'shop/edit_profile.html', {'form': form})

