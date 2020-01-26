from uuid import uuid1
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from core.models import SEO


class Category(SEO):
    title = models.CharField(max_length=250, unique=True, verbose_name='Название категории')

    def get_absolute_url(self):
        return reverse('catalogue_category', args=[self.slug])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class SubCategory(SEO):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='subcategories')
    title = models.CharField(max_length=250, unique=True, verbose_name='Название подкатегории')

    def get_absolute_url(self):
        return reverse('catalogue_subcategory', args=[self.category.slug, self.slug])

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
    in_stock = models.PositiveIntegerField(verbose_name='Количество')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateField(auto_now=True, verbose_name='Дата изменения')

    def get_absolute_url(self):
        subcategory_slug = self.subcategory.slug if self.subcategory else 'all'
        return reverse('catalogue_item', args=[self.category.slug, subcategory_slug, self.slug])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('created',)

    def __str__(self):
        return self.title

    def get_main_image(self):
        main_images = self.images.filter(is_main=True)
        if main_images.exists():
            main_image = main_images.first()
        else:
            main_image = self.images.first()
        return main_image
        

class Characteristic(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='characteristics')
    title = models.CharField(max_length=250, verbose_name='Название')
    value = models.CharField(max_length=250, verbose_name='Значение')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.title


class Option(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='options')
    title = models.CharField(max_length=250, verbose_name='Название')
    value = models.CharField(max_length=250, verbose_name='Значение')
    product_for = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Ссылка на товар', related_name='options_for', null=True, blank=True)

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Комплектация'

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='images')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/products/{0}'.format(filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    is_main = models.BooleanField(default=False, verbose_name='Главное изображение')

    image_medium = ImageSpecField(source='image',
                               processors=[ResizeToFill(330, 330)],
                               format='JPEG',
                               options={'quality': 90})
    
    image_small = ImageSpecField(source='image',
                               processors=[ResizeToFill(130, 130)],
                               format='JPEG',
                               options={'quality': 90})
    
    image_big = ImageSpecField(source='image',
                               processors=[ResizeToFill(690, 690)],
                               format='JPEG',
                               options={'quality': 90})

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return '{0}'.format(self.id)


class BarType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='offers')
    title = models.CharField(max_length=250, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    in_stock = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Тип брусков'
        verbose_name_plural = 'Типы брусков'

    def __str__(self):
        return self.title
