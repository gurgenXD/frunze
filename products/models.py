from django.db import models
from django.urls import reverse
from core.models import SEO


class Category(SEO):
    title = models.CharField(max_length=250, unique=True, verbose_name='Название категории')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class SubCategory(SEO):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='subcategories')
    title = models.CharField(max_length=250, unique=True, verbose_name='Название подкатегории')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    def get_absolute_url(self):
        return reverse('subcategory', args=[self.slug])

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.title


class Product(SEO):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, verbose_name='Подкатегория', related_name='products', null=True, blank=True)
    title = models.CharField(max_length=250, unique=True, verbose_name='Название товара')
    article = models.CharField(max_length=50, verbose_name='Артикул')
    price = models.PositiveIntegerField(verbose_name='Цена')
    desc = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateField(auto_now=True, verbose_name='Дата изменения')

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('created',)

    def __str__(self):
        return self.title