from django.db import models
from base.models import AbstractDateTimeModel
from django.core.mail import send_mail

# Create your models here.
class Subscribe(AbstractDateTimeModel):

    SUB_STATUSES = (
        ('sales', 'sales'),
        ('news', 'news'),
        ('material', 'material')
    )

    status = models.CharField("Статус подписки", choices=SUB_STATUSES, default="sales", max_length=20)

    # Если статус material - значит подписка на материал
    material = models.CharField("Название материала", max_length=255, blank=True)

    name = models.CharField("Имя или компания", blank=True, max_length=255)

    contact = models.CharField("Емайл пользователя, которому отправлять новости", max_length=255)

    def __str__(self) -> str:
        return self.contact

    def save(self, *args, **kwargs):
        """
        Если contact уже есть, то ничего не делаем
        """
        same_contacts = Subscribe.objects.filter(contact=self.contact).first()

        text = f'Новая подписка на скидки от {self.contact}'

        if self.material:
            text = f'Новая подписка на информацию о появлении товара от {self.contact} на материал {self.material}'

        # отправка сообщения, что человек подписался
        send_mail(
            'Новая подписка', 
            text,
            'bestrongwb@gmail.com',
            ['bestrongwb@gmail.com'],
            fail_silently=False)

        
        if not same_contacts:
            super().save(*args, **kwargs)