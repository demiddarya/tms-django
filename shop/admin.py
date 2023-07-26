from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Category
from .models import Profile
from .models import OrderEntry
from .models import Order


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'price']}),
        ('Information', {'fields': ['category']}),
    ]
    list_display = ['name', 'category']
    list_filter = ['name', 'category']
    search_fields = ['name', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [ProductInline]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderEntry)
class OrderEntryAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
