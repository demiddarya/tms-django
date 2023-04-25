from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/product', views.detail_product, name='info_product'),
    path('<int:category_id>/category', views.detail_category, name='infor_category')
]
