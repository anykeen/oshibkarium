from django.db import models
from ckeditor.fields import RichTextField

class Relationship(models.Model):
    parent = models.ForeignKey('Card', related_name='parent_messages', on_delete=models.PROTECT)
    child = models.ForeignKey('Card', related_name='child_messages', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Родственные ошибки'
        verbose_name = 'Родственные ошибки'

class Card(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Заголовок')
    slug = models.CharField(max_length=200, verbose_name = 'Slug', unique = True)
    category = models.ForeignKey('Category', verbose_name = 'Категория', on_delete=models.PROTECT, related_name = 'cards')
    image = models.ImageField(upload_to="img/", null=True, blank=True, verbose_name = 'Изображение')
    excerpt = models.TextField(verbose_name = 'Лид')
    description = RichTextField(verbose_name = 'Описание')
    fix = RichTextField(verbose_name = 'Как побороть ошибку?')
    info = RichTextField(verbose_name = 'Что еще прочесть?', blank = True)
    example = RichTextField(verbose_name = 'Дополнительные примеры (потренируйтесь на них)', blank = True)
    related = models.ManyToManyField('Card', through=Relationship)

    class Meta:
        verbose_name_plural = 'Карточки ошибок'
        verbose_name = 'Карточка ошибки'

    def __str__(self):
        return self.title
    