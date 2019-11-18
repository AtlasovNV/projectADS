# Generated by Django 2.2.7 on 2019-11-18 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectCompaignDesigner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_ad', models.CharField(choices=[('-', '-'), ('+', '+')], max_length=1)),
                ('namegroup', models.CharField(max_length=100)),
                ('frase', models.CharField(max_length=100)),
                ('header1', models.CharField(max_length=50)),
                ('header2', models.CharField(max_length=40)),
                ('text', models.TextField(max_length=100)),
                ('link', models.URLField()),
                ('sangezeigtlink', models.CharField(max_length=20)),
                ('bewerten', models.DecimalField(decimal_places=2, max_digits=6)),
                ('region', models.CharField(max_length=50)),
                ('headerfastlink_1', models.CharField(blank=True, max_length=30)),
                ('headerfastlink_2', models.CharField(blank=True, max_length=30)),
                ('headerfastlink_3', models.CharField(blank=True, max_length=30)),
                ('headerfastlink_4', models.CharField(blank=True, max_length=30)),
                ('textfstlink_1', models.CharField(blank=True, max_length=60)),
                ('textfstlink_2', models.CharField(blank=True, max_length=60)),
                ('textfstlink_3', models.CharField(blank=True, max_length=60)),
                ('textfstlink_4', models.CharField(blank=True, max_length=60)),
                ('linkfastlink_1', models.URLField(blank=True)),
                ('linkfastlink_2', models.URLField(blank=True)),
                ('linkfastlink_3', models.URLField(blank=True)),
                ('linkfastlink_4', models.URLField(blank=True)),
                ('verfeinerungen_1', models.CharField(blank=True, max_length=25)),
                ('verfeinerungen_2', models.CharField(blank=True, max_length=25)),
                ('verfeinerungen_3', models.CharField(blank=True, max_length=25)),
                ('verfeinerungen_4', models.CharField(blank=True, max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
