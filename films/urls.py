from django.urls import path
from . import views

urlpatterns = [
    path ('film_list/', views.film_list_view, name= 'film_list'),
    path ('film_list/<int:id>/', views.film_defail_view, name= 'film_detail'),
]
