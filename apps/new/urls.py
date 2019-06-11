from django.contrib import admin
from django.urls import path

from .views import *
app_name = 'new'
urlpatterns = [
    path('newlist/', NewList.as_view(), name='new_list'),
]
