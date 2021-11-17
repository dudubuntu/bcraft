from django.urls import path

from .views import *


app_name = 'statistics_app'
urlpatterns = [
    path('', init),
]