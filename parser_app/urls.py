from django.urls import path
from . import views

urlpatterns = [
    path('rezka_list/', views.RezkaListView.as_view(), name='rezka_list'),
    path('parser/', views.ParserFormView.as_view(), name='parser_form'), 
]
