from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Template
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        now = datetime.now()

        # template = Template(
        #     keywords='keywords',
        #     url='url',
        #     displayed_url='displayed_url',
        #     headline_1='headline_1',
        #     headline_2='headline_2',
        #     text='text',
        #     is_active=True,
        #     created=now,
        #     updated=now,
        #     fast_url_1='fast_url_1',
        #     description_1='description_1'
        # )
        # template.save()

        # templates = Template.objects.all()
        # for i in templates:
        #     print(i)

        templates = Template.get_all()
        # print(templates)
        for item in templates:
            print(item.pk, ' ', item)
        print('________________---------------____________-------------')
        # templates[0].delete()
        # for item in templates:
        #     print(item)

        # now = datetime.now()
        #
        # template = Template(
        #     keywords='keywords',
        #     url='url',
        #     displayed_url='displayed_url',
        #     headline_1='headline_1',
        #     headline_2='headline_2',
        #     text='text',
        #     # sort = models.IntegerField(verbose_name='номер объекта для сортировки', default=0, blank=True, null=False)
        #     is_active=True,
        #     created=now,
        #     updated=now,
        #     fast_url_1='fast_url_1',
        #     description_1='description_1'
        # )
        # template.save()