from django.contrib.admin.sites import site
from django.core.management.base import BaseCommand, CommandError
from catalog.models import Series, Collection, Material
import csv
from django.conf import settings
from django.db import transaction


class Command(BaseCommand):
    help = "Обновляет список продуктов в соответствии с прайс-листом, который лежит в catalog/management/commands/data.csv"

    @transaction.atomic
    def handle(self, *args, **options):
        with open(str(settings.BASE_DIR) + '/data.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            first_line = next(reader)

            series = Series.objects.create(name=first_line[1])
            collection = Collection.objects.create(series=series, name=first_line[2], size=first_line[5], price1=first_line[6], price2=first_line[7])
            Material.objects.create(num=first_line[0], collection=collection, color=first_line[3], item_number=first_line[4])

            for line in reader:
                if line[1] != series.name:
                    series = Series.objects.create(name=line[1])
                if line[2] != collection.name:
                    collection = Collection.objects.create(series=series, name=line[2], size=line[5], price1=line[6], price2=line[7])

                Material.objects.create(num=line[0], collection=collection, color=line[3], item_number=line[4])