from django.db import models
from base.models import AbstractDateTimeModel


class Series(models.Model):
    """
    Серия материала - Heritage, atelier, spectrum, textile
    """
    name = models.CharField("Серия: heritage/atelier итд", max_length=20)

    def __str__(self) -> str:
        return self.name


class Collection(models.Model):
    """
    Коллекция материала, состоит внутри серии
    """
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    name = models.CharField("Название коллекции", max_length=20)
    size = models.CharField("Размер", max_length=20, default='106/100')
    price1 = models.FloatField("Цена от 1 погонного метра")
    price2 = models.FloatField("Цена от 1 рулона")

    def __str__(self) -> str:
        return self.name + ' - ' + self.series.name


class Material(AbstractDateTimeModel):
    """
    Обычный материал, главное это артикул (item_number)
    """
    num = models.IntegerField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)

    item_number = models.CharField("Артикул", max_length=10, unique=True)

    img = models.ImageField('Картинка материала', upload_to="catalog", blank=True)

    def __str__(self) -> str:
        return self.color + ' - ' + self.item_number + ' - ' + self.collection.name