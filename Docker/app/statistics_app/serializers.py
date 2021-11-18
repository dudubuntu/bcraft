from typing_extensions import Required
from rest_framework import serializers

from .models import Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    cpc = serializers.FloatField(required=False)
    cpm = serializers.FloatField(required=False)
    
    class Meta:
        model = Statistics
        fields = ['date', 'views', 'clicks', 'cost', 'cpc', 'cpm']


class DateSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        setattr(self, 'from', serializers.DateField("YYYY-MM-DD", required=False))
        setattr(self, 'to', serializers.DateField("YYYY-MM-DD", required=False))
        return super().__init__(self, *args, **kwargs)