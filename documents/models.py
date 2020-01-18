from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def get_document_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(self.slug, ext)
        return 'documents/{0}'.format(filename)

    document = models.FileField(upload_to=get_document_url, max_length=250, verbose_name='Файл')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ('created',)

    def __str__(self):
        return self.title