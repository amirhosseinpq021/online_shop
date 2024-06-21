from django.contrib import admin

from .models import Product, Comment


# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active', 'is_featured', 'is_sale', 'cover', 'datetime_created', 'discount',
                    'discounted_price', 'sell_price')

    search_fields = ('id', 'title', 'is_featured', 'is_sale', 'discount',
                     'discounted_price', 'sell_price')

    list_editable = ('is_featured', 'is_sale', 'active', 'discount',
                     )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'user', 'product', 'is_active', 'stars', 'recommend')

    # search_fields = ('id',  )

    list_editable = ('user', 'product', 'is_active', 'stars', 'recommend'
                     )


admin.site.register(Product, ProductsAdmin)
admin.site.register(Comment, CommentAdmin)

