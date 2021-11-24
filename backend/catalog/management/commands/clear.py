from django.core.management.base import BaseCommand
from catalog.models import Series, Collection, Material
import csv
from django.conf import settings
from django.db import transaction


class Command(BaseCommand):
    help = "Обновляет список продуктов в соответствии с прайс-листом, который лежит в catalog/management/commands/data.csv"

    @transaction.atomic
    def handle(self, *args, **options):
        series = Series.objects.all()
        for i in series:
            i.delete()