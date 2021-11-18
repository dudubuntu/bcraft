from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import StatisticsView


app_name = 'statistics_app'

router = SimpleRouter()
router.register("", StatisticsView)

urlpatterns = router.urls