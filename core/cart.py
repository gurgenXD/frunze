from products.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.setdefault('cart', {})

    def add(self, product, price, quantity, max_q, bar_type):
        item = self.cart.get(product.id)
        if item not in self.cart:
            self.cart[product.id] = {
                'quantity': int(quantity),
                'price': int(price),
                'cost': int(price) * int(quantity),
                'title': product.title,
                'max_q': int(max_q),
                'product_id': product.id,
                'bar_type': bar_type,
                'absolute_url': product.get_absolute_url(),
                'main_image_url': product.get_main_image().image_small.url
            }
            self.save()

    def change_quantity(self, product_id, quantity):
        self.cart[product_id]['quantity'] = quantity
        self.cart[product_id]['cost'] = self.cart[product_id]['price'] * quantity
        self.save()

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def __iter__(self):
        for item in self.cart.values():
            yield item
    
    def keys(self):
        for item in self.cart.keys():
            yield item
    
    def values(self):
        for item in self.cart.values():
            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.values())

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.values())

    def clear(self):
        del self.session['cart']
        self.session.modified = True