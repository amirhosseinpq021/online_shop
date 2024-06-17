from django.contrib import admin

from .models import Product


# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active', 'is_featured', 'is_sale', 'cover', 'datetime_created',)
    search_fields = ('id', 'title', 'is_featured', 'is_sale',)
    list_editable = ('is_featured', 'is_sale', 'active')


admin.site.register(Product, ProductsAdmin)