from django.db import models
from tinymce.models import HTMLField

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Заголовок')
    slug = models.CharField(max_length=200, verbose_name = 'Slug')
    content = HTMLField(verbose_name = 'Контент')

    class Meta:
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страница'

    def __str__(self):
        return self.title