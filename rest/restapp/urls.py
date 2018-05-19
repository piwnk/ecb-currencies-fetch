from django.contrib import admin
from django.urls import path

from restapp import views

urlpatterns = [
    path('api/currencies', views.get_currencies)
]
