from django.contrib import admin
from django.utils.html import format_html

from .models import Product, Comment


# Register your models here.


class ProductCommentInline(admin.TabularInline):
    model = Comment
    fields = ['user', 'text', 'is_active', 'stars', 'recommend']
    extra = 10


class ProductsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="100" style="border-radius:50px" />'.format(object.cover.url))

    thumbnail.short_description = 'photo'

    list_display = ('title', 'price', 'active', 'is_featured', 'is_sale', 'thumbnail', 'datetime_created', 'discount',
                    'discounted_price',  'the_amount_of_discount', 'sales_amount_after_discount', 'all_discount')

    search_fields = ('id', 'title', 'is_featured', 'is_sale', 'discount',
                     'discounted_price', 'the_amount_of_discount', 'sales_amount_after_discount')

    list_editable = ('is_featured', 'is_sale', 'active', 'discount', 'the_amount_of_discount',
                     )

    inlines = [
        ProductCommentInline,
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'user', 'product', 'is_active', 'stars', 'recommend')

    # search_fields = ('id',  )

    list_editable = ('user', 'product', 'is_active', 'stars', 'recommend'
                     )









admin.site.register(Product, ProductsAdmin)
admin.site.register(Comment, CommentAdmin)

