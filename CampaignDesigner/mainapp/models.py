from django.db import models
from django.conf import settings


class Campaign (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='создана', auto_now_add=True)
    update = models.DateTimeField(verbose_name='обновлена', auto_now=True)


class GroupName(models.Model):
    name_group = models.CharField(max_length=100, blank=True)


class Header (models.Model):
    header1 = models.CharField(max_length=50)
    header2 = models.CharField(max_length=40)


class SharedDataGroup(models.Model):
    text = models.TextField(max_length=100)
    link = models.URLField(max_length=200)
    sangezeigt_link = models.CharField(max_length=20)
    bewerten = models.DecimalField(max_digits=6, decimal_places=2)


class Regions(models.Model):
    region = models.CharField(max_length=50)


class FastLink(models.Model):
    header_fast_link_1 = models.CharField(max_length=30, blank=True)
    header_fast_link_2 = models.CharField(max_length=30, blank=True)
    header_fast_link_3 = models.CharField(max_length=30, blank=True)
    header_fast_link_4 = models.CharField(max_length=30, blank=True)
    text_fast_link_1 = models.CharField(max_length=60, blank=True)
    text_fast_link_2 = models.CharField(max_length=60, blank=True)
    text_fast_link_3 = models.CharField(max_length=60, blank=True)
    text_fast_link_4 = models.CharField(max_length=60, blank=True)
    link_fast_link_1 = models.URLField(max_length=200, blank=True)
    link_fast_link_2 = models.URLField(max_length=200, blank=True)
    link_fast_link_3 = models.URLField(max_length=200, blank=True)
    link_fast_link_4 = models.URLField(max_length=200, blank=True)
    verfeinerungen_1 = models.CharField(max_length=25, blank=True)
    verfeinerungen_2 = models.CharField(max_length=25, blank=True)
    verfeinerungen_3 = models.CharField(max_length=25, blank=True)
    verfeinerungen_4 = models.CharField(max_length=25, blank=True)


class Frases (models.Model):
    PLUS = '+'
    MINUS = '-'

    ADDITIONAL_AD_CHOICES = (
        (MINUS, '-'),
        (PLUS, '+'),
    )

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    additional_ad = models.CharField(max_length=1,
                                     choices=ADDITIONAL_AD_CHOICES)
    frase = models.CharField(max_length=100)
    region = models.ForeignKey('Regions', on_delete=models.CASCADE,
                               null=True)
    name_group = models.ForeignKey('GroupName', on_delete=models.CASCADE,
                                   null=True)
    headers = models.ForeignKey('Header', on_delete=models.CASCADE,
                                null=True)
    shared_data_group = models.ForeignKey('SharedDataGroup',
                                          on_delete=models.CASCADE,
                                          null=True)
    fast_link = models.ForeignKey('FastLink', on_delete=models.CASCADE,
                                  null=True)


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
