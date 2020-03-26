from django.db import models
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField, get_thumbnail


class Example(models.Model):
    wrong = models.TextField('Ошибочный пример', blank=True)
    correct = models.TextField('Правильный ответ', blank=True)
    card = models.ForeignKey('Card', on_delete=models.CASCADE, related_name='examples', blank = True, null = True)

    class Meta:
        verbose_name_plural = 'Примеры'
        verbose_name = 'Пример'

class Relationship(models.Model):
    parent = models.ForeignKey('Card', related_name='parent_messages', on_delete=models.SET_NULL, null=True, blank=True)
    child = models.ForeignKey('Card', related_name='child_messages', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Родственные ошибки'
        verbose_name = 'Родственная ошибка'

class Card(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.CharField('Slug', max_length=200, unique = True)
    index = models.CharField('Индекс', max_length=10, blank=True)
    category = models.ForeignKey('Category', verbose_name = 'Категория', on_delete=models.PROTECT, related_name = 'cards')
    image = ImageField('Изображение', upload_to="img/", null=True, blank=True)
    excerpt = models.TextField('Лид')
    description = RichTextField('Описание')
    fix = RichTextField('Как побороть ошибку?')
    info = RichTextField('Что еще прочесть?', blank = True)
    example = RichTextField('Дополнительные примеры (потренируйтесь на них)', blank = True)
    published = models.BooleanField('Опубликован', default=False)
    related = models.ManyToManyField('Card', through=Relationship)


    def image_tag(self):
        if self.image:
            return u'<img src="%s%s" />' % (settings.MEDIA_URL,
                                            get_thumbnail(self.image, '90x90'))
        else:
            return 'без картинки'
    image_tag.short_description = 'картинка'
    image_tag.allow_tags = True


    class Meta:
        verbose_name_plural = 'Карточки ошибок'
        verbose_name = 'Карточка ошибки'
    
    

    def __str__(self):
        return self.title
    