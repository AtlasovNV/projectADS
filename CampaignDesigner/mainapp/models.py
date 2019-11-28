from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save

# Create your models here.


class Template(models.Model):
    """ Класс Шаблона объявления """
    class Meta:
        ordering = ('updated', 'created')
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'

    keywords = models.CharField(verbose_name='Ключевые слова', max_length=255, blank=False, null=False, default='#')
    url = models.CharField(verbose_name='Ссылка на сайт', help_text='ТЕСТ ТЕСТ', max_length=255, blank=False, null=False, default='#')
    displayed_url = models.CharField(verbose_name='Отображаемая ссылка', max_length=255, blank=False, null=False, default='#')
    headline_1 = models.CharField(verbose_name='Первый заголовок', max_length=35)
    headline_2 = models.CharField(verbose_name='Второй заголовок', max_length=35, default='Посмотрите на сайте!')
    text = models.TextField(verbose_name='Текст шаблона', blank=True, null=True)
    # sort = models.IntegerField(verbose_name='номер объекта для сортировки', default=0, blank=True, null=False)
    is_active = models.BooleanField(verbose_name='активен ли шаблон', default=True, db_index=True)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    fast_url_1 = models.CharField(verbose_name='Быстрая ссылка 1', max_length=255, blank=True, null=True)
    description_1 = models.CharField(verbose_name='Описание 1-й ссылки', max_length=255, blank=True, null=True)
    fast_url_2 = models.CharField(verbose_name='Быстрая ссылка 2', max_length=255, blank=True, null=True)
    description_2 = models.CharField(verbose_name='Описание 2-й ссылки', max_length=255, blank=True, null=True)
    fast_url_3 = models.CharField(verbose_name='Быстрая ссылка 3', max_length=255, blank=True, null=True)
    description_3 = models.CharField(verbose_name='Описание 3-й ссылки', max_length=255, blank=True, null=True)
    fast_url_4 = models.CharField(verbose_name='Быстрая ссылка 4', max_length=255, blank=True, null=True)
    description_4 = models.CharField(verbose_name='Описание 4-й ссылки', max_length=255, blank=True, null=True)
    refinements = models.TextField(verbose_name='Уточнения', max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.headline_1}' if self.headline_1 else ''

    def delete(self, **kwargs):  # или может *args
        if 'force' in kwargs:
            super().delete()
        else:
            self.is_active = False
            self.save()

    # Убираем из каталога неактивные шаблоны
    @staticmethod
    def get_active():
        return Template.objects.filter(is_active=True)

    @staticmethod
    def get_all():
        return Template.objects.all()
