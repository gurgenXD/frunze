from django.db import models


class SEO(models.Model):
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    seo_desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    seo_kwrds = models.CharField(max_length=250, verbose_name='Keywords', blank=True)
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    class Meta:
        abstract = True


class Order(models.Model):
    position = models.PositiveIntegerField(verbose_name='Позиция', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.position is None:
            try:
                last = self.objects.order_by('-position')[0]
                self.position = last.position + 1
            except:
                self.position = 0
        return super(Order, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ('position',)
