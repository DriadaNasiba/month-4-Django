from django.urls import path
from . import views

app_name ='users'


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthloginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('user_list/', views.UserListView.as_view(), name='user_list'),
]
