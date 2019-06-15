from django.urls import path

from .views import *
app_name = 'server'
urlpatterns = [
    path('', Server.as_view(), name='index')
]
