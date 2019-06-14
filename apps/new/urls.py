from django.contrib import admin
from django.urls import path

from .views import *
app_name = 'new'
urlpatterns = [
    path('newlist/', NewList.as_view(), name='new_list'),
    path('article/<str:classify>/<int:new_id>/', NewArticle.as_view(), name='article'),
]
