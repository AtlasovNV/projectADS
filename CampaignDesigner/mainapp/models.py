from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save

# Create your models here.


class Template(models.Model):
    """ Класс Шаблона объявления """
    class Meta:
        # ordering = ('-is_active', 'sort', 'name')
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'

    keywords = models.CharField(verbose_name='Ключевые слова', max_length=255, blank=False, null=False, default='#')
    url = models.CharField(verbose_name='Ссылка на сайт', max_length=255, blank=False, null=False, default='#')
    displayed_url = models.CharField(verbose_name='Отображаемая ссылка', max_length=255, blank=False, null=False, default='#')
    headline_1 = models.CharField(verbose_name='Первый заголовок', max_length=35)
    headline_2 = models.CharField(verbose_name='Второй заголовок', max_length=35, default='Посмотрите на сайте!')
    text = models.TextField(verbose_name='Текст шаблона', blank=True, null=True)
    # sort = models.IntegerField(verbose_name='номер объекта для сортировки', default=0, blank=True, null=False)
    is_active = models.BooleanField(verbose_name='активен ли шаблон', default=True, db_index=True)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)

    def __str__(self):
        return f'{self.headline_1}' if self.headline_1 else ''

    def delete(self, **kwargs):  # или может *args
        if 'force' in kwargs:
            super().delete()
        else:
            self.is_active = False
            self.save()