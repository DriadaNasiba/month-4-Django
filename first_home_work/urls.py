from django.urls import path
from . import views

urlpatterns = [
    path ( '', views.fist_home_wokr, name= 'index'),
]