from django.db import models

from .time_model import TimeModel
from .validators import mobile_number_validator


class MemoUser(TimeModel):
    username = models.CharField(
        max_length=80,
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

    class Meta:
        verbose_name = 'کاربر خاطره نگار'
        verbose_name_plural = "کابر های خاطره نگار"
