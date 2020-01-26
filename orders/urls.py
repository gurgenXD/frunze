from django.urls import path
from orders.views import *


urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('change-qty/', ChangeQtyView.as_view(), name='change_qty_cart'),
    path('order-add/', OrderAddView.as_view(), name='order_add'),
    path('cart/', CartView.as_view(), name='cart'),
    path('order-done/', OrderDoneView.as_view(), name='order_done'),
]
