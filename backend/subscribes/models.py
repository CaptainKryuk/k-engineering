from django.db import models
from base.models import AbstractDateTimeModel

# Create your models here.
class Subscribe(AbstractDateTimeModel):

    SUB_STATUSES = (
        ('sales', 'sales'),
        ('news', 'news')
    )

    status = models.CharField("Статус подписки", choices=SUB_STATUSES, default="sales", max_length=20)

    email = models.EmailField("Емайл пользователя, которому отправлять новости")

    def __str__(self) -> str:
        return self.email

    def save(self, *args, **kwargs):
        """
        Если email уже есть, то ничего не делаем
        """
        same_emails = Subscribe.objects.filter(email=self.email).first()
        if not same_emails:
            super().save(*args, **kwargs)