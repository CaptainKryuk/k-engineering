from django.core.management.base import BaseCommand, CommandError
from catalog.models import Series, Collection, Material
from django.db import transaction
from django.conf import settings
import os
from pathlib import Path, PurePath
from django.core.files import File

class Command(BaseCommand):

    help = "Пробегается по папке с картинками и добавляет их по артикулу в img Material"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        path = PurePath(settings.BASE_DIR).joinpath('media').joinpath('catalog')
        files = []
        for address, dirs, files in os.walk(path):
            files = files 

        materials = Material.objects.all()

        for material in materials:
            img_path = ''
            if f'{material.item_number}.jpeg' in files:
                img_path = f'{material.item_number}.jpeg'
            elif f'{material.item_number}.jpg' in files:
                img_path = f'{material.item_number}.jpg'

            
            full_img_path = Path(path).joinpath(img_path)
            if Path.is_file(full_img_path):
                material.img = f'catalog/{img_path}'
                material.save()

            print(material.img)