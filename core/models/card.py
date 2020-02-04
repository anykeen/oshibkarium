from django.db import models
from .category import Category
from tinymce.models import HTMLField

class Relationship(models.Model):
    parent = models.ForeignKey('Card', related_name='parent_messages', on_delete=models.CASCADE)
    child = models.ForeignKey('Card', related_name='child_messages', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Родственные ошибки'
        verbose_name = 'Родственные ошибки'

class Card(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Заголовок')
    slug = models.CharField(max_length=200, verbose_name = 'Slug')
    category = models.ForeignKey(Category, verbose_name = 'Категория', on_delete=models.CASCADE)
    excerpt = models.TextField(verbose_name = 'Лид')
    description = HTMLField(verbose_name = 'Описание')
    fix = HTMLField(verbose_name = 'Как с этим справиться?')
    info = HTMLField(verbose_name = 'Что еще прочесть?')
    example = HTMLField(verbose_name = 'Дополнительные примеры')
    related = models.ManyToManyField('Card', through=Relationship)

    class Meta:
        verbose_name_plural = 'Карточки ошибок'
        verbose_name = 'Карточка ошибки'

    def __str__(self):
        return self.title
    