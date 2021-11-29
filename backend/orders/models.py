from django.db import models
from base.models import AbstractDateTimeModel
from django.core.mail import send_mail


class Order(AbstractDateTimeModel):

    material = models.CharField("Название материала", max_length=255)

    quantity = models.CharField("Количество погонных метров", max_length=255, default=10)

    contact = models.CharField('Контактная информация', max_length=255)

    name = models.CharField("Имя или компания", max_length=255)

    def __str__(self) -> str:
        return self.name + ' ' + self.contact + ' ' + self.material


    def save(self, *args, **kwargs):
        """
        Просто отправка заявки на почту
        """
        send_mail(
            'НОВЫЙ ЗАКАЗ!!!', 
            f'Новый заказ на {self.material} количество {self.quantity} от {self.contact} {self.name}',
            'bestrongwb@gmail.com',
            ['bestrongwb@gmail.com'],
            fail_silently=False)
        super().save(*args, **kwargs)