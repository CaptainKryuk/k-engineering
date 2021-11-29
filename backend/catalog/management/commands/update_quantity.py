
from django.core.management.base import BaseCommand
from django.conf import settings
import csv
from catalog.models import Material
from django.db import transaction


class Command(BaseCommand):

    help = "Обновляет количество всех продуктов"
    
    @transaction.atomic
    def handle(self, *args, **kwargs):
        with open(str(settings.BASE_DIR)+ '/data2.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            result = {}

            for line in reader:
                # if line[0] not in result:
                #     result[line[0]] = line[1]
                # else:
                #     result[line[0]] += line[1]

                if line[1]:
                    item = Material.objects.filter(item_number=line[0]).first()
                    if item:
                        item.quantity = float(line[1])
                        item.save()
