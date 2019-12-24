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
    header1 = models.CharField(verbose_name='Заголовок 1', max_length=50)
    header2 = models.CharField(verbose_name='Заголовок 2', max_length=40)


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
                                     choices=ADDITIONAL_AD_CHOICES,
                                     blank=True)
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
