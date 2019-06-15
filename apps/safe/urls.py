from django.urls import path

from .views import Safe
app_name = 'safe'
urlpatterns = [
    path('', Safe.as_view(), name='index')
]
