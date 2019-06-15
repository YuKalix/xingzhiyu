from django.urls import path

from .views import *
app_name = 'about_us'
urlpatterns = [
    path('', AboutUs.as_view(), name='index')
]
