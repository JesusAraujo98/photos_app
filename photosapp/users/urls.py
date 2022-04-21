from django.urls import path
from . import views

app_name= 'users'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name= 'logout'),
    path('', views.index_view, name= 'index'),
    path('profile/', views.my_profile_view, name = 'profile'),
    path('clients/', views.create_client_view, name = 'clients'),
]