from uuid import uuid4

from django.db import models

from .time_model import TimeModel
from .validators import mobile_number_validator


class MemoUser(TimeModel):
    username = models.CharField(
        max_length=80,
        unique=True,
        verbose_name='یوزرنیم'
    )

    first_name = models.CharField(
        max_length=60,
        verbose_name='نام'
    )

    last_name = models.CharField(
        max_length=60,
        verbose_name='نام خانوادگی'
    )

    password = models.CharField(
        max_length=60,
        verbose_name='پسورد'
    )

    email = models.EmailField(
        verbose_name='ایمیل'
    )

    phone_number = models.CharField(
        max_length=11,
        verbose_name='شماره تلفن',
        validators=(mobile_number_validator,),
    )

    birthday_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='تاریخ تولد'
    )

    token = models.CharField(
        null=True,
        blank=True,
        max_length=40,
        verbose_name='توکن'
    )

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.pk:
            self.token = str(uuid4())
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'کاربر خاطره نگار'
        verbose_name_plural = "کابر های خاطره نگار"
