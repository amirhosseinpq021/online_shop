from django import template

register = template.Library()


@register.filter
def only_active_comment(comments):
    return comments.filter(is_active=True)


@register.filter
def sort_best_sell_product(product):
    return product.filter(is_sale=True).order_by('-datetime_created')[:4]


@register.filter
def sort_product_latest(product):
    return product.order_by('-datetime_created')[:4]


@register.filter
def sort_product_latest_show(product):
    return product.order_by('-datetime_created')
