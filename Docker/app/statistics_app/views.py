import datetime

from django.db.models.query import QuerySet
from django.utils import timezone
from django.shortcuts import render
from django.db.models import Count, Sum, F, Case, When
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets

from .backend import ListAPIView
from .serializers import StatisticsSerializer, DateSerializer
from .filters import StatisticsFilter
from .models import Statistics


class StatisticsView(ListAPIView,
                     viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StatisticsSerializer
    filter_backends = [StatisticsFilter]
    queryset = Statistics.objects.all()

    def get_dates(self, request):
        """Берет даты из входящего json. Поля from, to
        """
        d1, d2 = datetime.date.fromordinal(1), timezone.now()
        ser = DateSerializer(data=request.data)

        if ser.is_valid():
            data = ser.validated_data
            d1, d2 = data.get("from", d1), data.get("to", d2)
            return d1, d2, {}
        return d1, d2, ser.errors


    def get_queryset(self, d1=None, d2=None):
        """Аннотация полей cpc, cpm
        """
        d1, d2, _ = self.get_dates(self.request)

        if d1 and d2 and len(self.queryset) != 0:
            qs = Statistics.objects.filter(date__gte=d1, date__lte=d2).values('date') \
                                   .annotate(views=Sum('views'), clicks=Sum('clicks'), cost=Sum('cost'), \
                                             cpc=Case(When(clicks=0, then=0.0), default=(F('cost') / F('clicks'))),\
                                             cpm=Case(When(views=0, then=0.0), default=(F('cost') / F('views') * 1000)))
            return qs
        return QuerySet(model=Statistics)

    def list(self, request, *args, **kwargs):
        """Возвращает список со статистикой по дням
        """
        self.request = request
        return super().list(request, *args, **kwargs)

    @action(["DELETE"], detail=False)
    def reset(self, request, *args, **kwargs):
        """Обнуляет статистику
        """
        self.queryset.delete()
        return Response(status=status.HTTP_201_CREATED)

    @action(["POST"], detail=False)
    def save(self, request, *args, **kwargs):
        """Сохраняет данные статистики за определенную дату
        """
        ser = StatisticsSerializer(data=request.data)
        if ser.is_valid():
            obj = ser.save()
            return Response(data=StatisticsSerializer(obj).data, status=status.HTTP_201_CREATED)
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)