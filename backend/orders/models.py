from django.db import models
from base.models import AbstractDateTimeModel
# Create your models here.


class Order(AbstractDateTimeModel):

    material = models.CharField("Название материала", max_length=255)

    quantity = models.CharField("Количество погонных метров", max_length=255, default=10)

    contact = models.CharField('Контактная информация', max_length=255)

    name = models.CharField("Имя или компания", max_length=255)

    def __str__(self) -> str:
        return self.name + ' ' + self.contact + ' ' + self.material