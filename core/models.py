from django.db import models
from contacts.models import Phone
from uuid import uuid1


class SEO(models.Model):
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    seo_desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    seo_kwrds = models.CharField(max_length=250, verbose_name='Keywords', blank=True)
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    class Meta:
        abstract = True


class Position(models.Model):
    position = models.PositiveIntegerField(verbose_name='Позиция', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.position is None:
            try:
                last = self.objects.order_by('-position')[0]
                self.position = last.position + 1
            except:
                self.position = 0
        return super(Position, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ('position',)


class Index(SEO):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    phone = models.ForeignKey(Phone, on_delete=models.SET_NULL, verbose_name='Телефон', null=True)
    slogan = models.CharField(max_length=250, verbose_name='Слоган')
    desc = models.TextField(verbose_name='Описание')
    about = models.TextField(verbose_name='О нас')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    text = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(verbose_name='Показывать на сайте', default=True)

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/advantage/{0}'.format(filename)

    image = models.FileField(max_length=250, upload_to=get_picture_url, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self):
        return self.title