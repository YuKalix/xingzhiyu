from django.urls import path

from .views import *
app_name = 'success_case'
urlpatterns = [
    path('', SuccessCase.as_view(), name='index')
]
