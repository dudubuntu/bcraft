from django.db import models

from .validators import positive_value_validation


class Statistics(models.Model):
    date = models.DateField('Дата')
    views = models.PositiveIntegerField('Количество показов', default=0)
    clicks = models.PositiveIntegerField('Количество кликов', default=0)
    cost = models.FloatField('Стоимость клика', default=0, validators=[positive_value_validation])

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'