from django.db import models
from ckeditor.fields import RichTextField
from django.apps import apps

STATUSES = (
    ('published','Published'),
    ('declined', 'Declined'),
    ('pending','Pending'),
)

class Cliche(models.Model):
    cliche = models.CharField('Штамп', max_length=200)
    comment = RichTextField('Комментарий', blank = True)
    rating = models.IntegerField('Рейтинг', default=0, blank=True)
    author = models.ForeignKey('users.Profile', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=9, choices=STATUSES, default='published')

    class Meta:
        verbose_name_plural = 'Штампы'
        verbose_name = 'Штамп'

    def __str__(self):
        return self.cliche
