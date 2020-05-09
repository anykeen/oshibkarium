from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Заголовок')
    slug = models.CharField(max_length=200, verbose_name = 'Slug', unique = True)
    seo_title = models.CharField('СЕО-заголовок', max_length=200, blank = True)
    seo_desc = models.CharField('СЕО-описание', max_length=200, blank = True)
    content = RichTextField(verbose_name = 'Контент')

    class Meta:
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страница'

    def __str__(self):
        return self.title