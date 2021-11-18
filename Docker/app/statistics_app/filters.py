from django_filters.rest_framework import FilterSet
from django_filters import filters

from .models import Statistics


class StatisticsFilter(FilterSet):
    o = filters.OrderingFilter(
        fields = (
            ('date', 'date'),
            ('views', 'views'),
            ('clicks', 'clicks'),
            ('cost', 'cost'),
            ('cpc', 'cpc'),
            ('cpm', 'cpm'),
        )
    )

    class Meta:
        models = Statistics
        fields = ['date', 'views', 'clicks', 'cost', 'cpc', 'cpm']