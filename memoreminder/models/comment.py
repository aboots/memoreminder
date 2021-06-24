from django.db import models

from .time_model import TimeModel


class Comment(TimeModel):
    memo_user = models.ForeignKey(
        'memoreminder.MemoUser',
        on_delete=models.CASCADE,
        verbose_name='کاربر'
    )

    text = models.TextField(
        max_length=300,
        verbose_name='متن'
    )

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = "کامنت ها"
