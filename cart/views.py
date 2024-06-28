from django.shortcuts import render
from .cart import Cart
from django.shortcuts import get_object_or_404
from products.models import Product
from .forms import AddToCartProductForm
from django.shortcuts import redirect


def cart_detail_view(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart_detail.html', context)


def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add_to_cart(product, quantity)

    return redirect('cart:cart_detail')
