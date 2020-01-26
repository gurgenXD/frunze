from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('total_price',)
    fields = ('product', 'bar_type', 'price', 'quantity', 'total_price')
    classes = ('grp-collapse grp-closed',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('full_name', 'phone', 'email', 'total_price', 'created', 'updated'),
        }),
    )

    readonly_fields = ('total_price', 'created', 'updated')
    inlines = (OrderItemInline,)
    list_display = ('full_name', 'phone', 'email', 'total_price', 'created', 'updated')
    search_fields = ('full_name', 'email',)