from decimal import Decimal

from products.models import Product


class Cart:
    def __init__(self, request):
        """
        initialize the cart
        """
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add_to_cart(self, product, quantity=1):
        """add product to cart if it exists"""

        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}

        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """Mark session as modified to save change"""
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            yield item

    def __len__(self):
        # return len((self.cart.keys()))
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Remove all items from the cart.
        """
        del self.session['cart']
        self.save()

    def get_sub_total_price(self):
        # return sum(Decimal(item['price_with_vat']) * item['quantity'] for item in self.cart.values())
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return sum([product.price_with_vat for product in products])
