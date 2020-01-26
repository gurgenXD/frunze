from django.db import models
from products.models import Product


class Order(models.Model):
    full_name = models.CharField(max_length=250, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='E-mail')
    
    total_price = models.PositiveIntegerField(default=0, verbose_name='Итоговая стоимость', help_text='Посчитается при сохранении.')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ №{0}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ', related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    bar_type = models.CharField(max_length=250, verbose_name='Тип брусков', null=True, blank=True)
    total_price = models.PositiveIntegerField(default=0, verbose_name='Стоимость', help_text='Посчитается при сохранении.')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def __str__(self):
        return '{0}'.format(self.id)
    