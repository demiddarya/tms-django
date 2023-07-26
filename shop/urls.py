
from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('products', views.products, name='products'),
    path('product/<int:product_id>', views.detail_product, name='detail_product'),
    path('category/<int:category_id>', views.detail_category, name='detail_category'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('register/', views.register, name='register'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('profile/<int:user_id>', views.profile_info, name='profile'),
    path('edit_profile/<int:user_id>', views.edit_profile, name='edit_profile')
]
