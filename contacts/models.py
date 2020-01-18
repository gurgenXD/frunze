from django.db import models


class Address(models.Model):
    value = models.CharField(max_length=250, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.value


class Phone(models.Model):
    value = models.CharField(max_length=20, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return self.value


class Fax(models.Model):
    value = models.CharField(max_length=20, verbose_name='Факс')

    class Meta:
        verbose_name = 'Факс'
        verbose_name_plural = 'Факсы'

    def __str__(self):
        return self.value


class Email(models.Model):
    value = models.EmailField(max_length=250, verbose_name='Почта')

    class Meta:
        verbose_name = 'Почта'
        verbose_name_plural = 'Почта'

    def __str__(self):
        return self.value


class MapCode(models.Model):
    value = models.TextField(verbose_name='Карта')

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return self.value


class Requisite(models.Model):
    full_name = models.CharField(max_length=250, verbose_name='Полное наименование')
    legal_address = models.CharField(max_length=250, verbose_name='Юридический (фактический) адреc')
    payment_account = models.CharField(max_length=25, verbose_name='Расчетный счет')
    correspondent_account = models.CharField(max_length=25, verbose_name='Корреспондентский счет')
    bank = models.CharField(max_length=250, verbose_name='Банк')
    inn = models.CharField(max_length=15, verbose_name='ИНН')
    kpp = models.CharField(max_length=15, verbose_name='КПП')
    bik = models.CharField(max_length=15, verbose_name='БИК')
    okpo = models.CharField(max_length=15, verbose_name='ОКПО')
    general_manager = models.CharField(max_length=250, verbose_name='Генеральный директор')
    basis = models.CharField(max_length=250, verbose_name='Действующий на основании')

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'

    def __str__(self):
        return self.full_name
