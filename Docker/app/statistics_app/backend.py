from rest_framework.generics import GenericAPIView as DefaultGenericAPIView
from rest_framework.generics import ListAPIView


class GenericAPIView(DefaultGenericAPIView):
    """Дефолтный класс бросает ошибку при инициализации StatisticsFilter без queryset`а

                queryset = self._meta.model._default_manager.all()
            AttributeError: 'NoneType' object has no attribute '_default_manager'

        Также, поле для сортировки берется из request.GET
    """
    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend(self.request.GET, queryset).qs
        return queryset


class ListAPIView(GenericAPIView,
                  ListAPIView):
    pass