from django.urls import path

from .views import *
app_name = 'safe'
urlpatterns = [
    path('', Safe.as_view(), name='index')
]
