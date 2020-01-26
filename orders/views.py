from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from core.models import MailToString
from core.cart import Cart
from products.models import Product
from orders.forms import OrderForm
from orders.models import OrderItem


class AddToCartView(View):
    @staticmethod
    def get(request):
        product_id = int(request.GET.get('product_id'))
        price = int(request.GET.get('price').replace(' ', ''))
        quantity = int(request.GET.get('quantity'))
        max_q = int(request.GET.get('max_q'))
        bar_type = request.GET.get('bar_type')

        product = get_object_or_404(Product, id=product_id)

        cart = Cart(request)
        cart.add(product, price, quantity, max_q, bar_type)

        context = {
            'cart_len': len(cart),
        }
        return JsonResponse(context)


class RemoveFromCartView(View):
    @staticmethod
    def get(request):
        product_id = request.GET.get('product_id')

        cart = Cart(request)
        cart.remove(product_id)

        context = {
            'cart_len': len(cart),
        }
        return JsonResponse(context)


class ChangeQtyView(View):
    @staticmethod
    def get(request):
        product_id = request.GET.get('product_id')
        quantity = int(request.GET.get('quantity'))

        cart = Cart(request)
        cart.change_quantity(product_id, quantity)

        cost = '{:,}'.format(cart.cart[product_id]['cost']).replace(',', ' ')

        context = {
            'cart_len': len(cart),
            'cost': cost,
        }
        return JsonResponse(context)


class CartView(View):
    @staticmethod
    def get(request):
        cart = Cart(request)
        order_form = OrderForm()

        context = {
            'cart': list(cart),
            'order_form': order_form,
        }
        return render(request, 'orders/cart.html', context)


class OrderDoneView(View):
    @staticmethod
    def get(request):
        return render(request, 'orders/order-done.html', {})


class OrderAddView(View):
    @staticmethod
    def post(request):
        order_form = OrderForm(request.POST)
        cart = Cart(request)
        
        if order_form.is_valid():
            try:
                new_order = order_form.save(commit=False)
                new_order.total_price = cart.get_total_price()
                new_order.save()

                for item in cart:
                    product = Product.objects.get(id=int(item['product_id']))
                    OrderItem.objects.create(
                        order=new_order,
                        product=product,
                        price=item['price'],
                        quantity=item['quantity'],
                        total_price=item['cost'],
                        bar_type=item['bar_type']
                    )

                current_site = get_current_site(request)
                mail_subject = 'Новый заказ на сайте: ' + current_site.domain
                message = render_to_string('email_messages/order_message.html', {
                    'domain': current_site.domain,
                    'order': new_order,
                })

                to_email = MailToString.objects.first().email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                cart.clear()
                status = 1
            except Exception as e:
                print(e)
                status = 0
        else:
            status = 0
        
        context = {
            'status': status,
        }
        return JsonResponse(context)
