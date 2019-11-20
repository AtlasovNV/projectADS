from django.db import models
from django.conf import settings


class CompaignFrases (models.Model):
    PLUS = '+'
    MINUS = '-'

    ADDITIONAL_AD_CHOICES = (
        (MINUS, '-'),
        (PLUS, '+'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    additional_ad = models.CharField(max_length=1,
                                     choices=ADDITIONAL_AD_CHOICES)
    namegroup = models.CharField(max_length=100)
    frase = models.CharField(max_length=100)
    header1 = models.CharField(max_length=50)
    header2 = models.CharField(max_length=40)
    text = models.TextField(max_length=100)
    link = models.URLField(max_length=200)
    sangezeigtlink = models.CharField(max_length=20)
    bewerten = models.DecimalField(max_digits=6, decimal_places=2)
    region = models.CharField(max_length=50)
    headerfastlink_1 = models.CharField(max_length=30, blank=True)
    headerfastlink_2 = models.CharField(max_length=30, blank=True)
    headerfastlink_3 = models.CharField(max_length=30, blank=True)
    headerfastlink_4 = models.CharField(max_length=30, blank=True)
    textfstlink_1 = models.CharField(max_length=60, blank=True)
    textfstlink_2 = models.CharField(max_length=60, blank=True)
    textfstlink_3 = models.CharField(max_length=60, blank=True)
    textfstlink_4 = models.CharField(max_length=60, blank=True)
    linkfastlink_1 = models.URLField(max_length=200, blank=True)
    linkfastlink_2 = models.URLField(max_length=200, blank=True)
    linkfastlink_3 = models.URLField(max_length=200, blank=True)
    linkfastlink_4 = models.URLField(max_length=200, blank=True)
    verfeinerungen_1 = models.CharField(max_length=25, blank=True)
    verfeinerungen_2 = models.CharField(max_length=25, blank=True)
    verfeinerungen_3 = models.CharField(max_length=25, blank=True)
    verfeinerungen_4 = models.CharField(max_length=25, blank=True)