from django.urls import path

from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.homepage, name='homepage'),
]
