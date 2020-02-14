from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Заголовок')
    slug = models.CharField(max_length=200, verbose_name = 'Slug', unique = True)
    num = models.PositiveIntegerField(verbose_name = 'Порядковый номер колонки', blank = True)
    description = models.TextField(blank=True, verbose_name = 'Описание')

    class Meta:
        verbose_name_plural = 'Категории ошибок'
        verbose_name = 'Категория ошибки'

    def __str__(self):
        return self.title