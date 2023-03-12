from django.urls import path
from . import views

app_name = "home_app"
urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('45', views.home, name='home'),
    path('', views.index, name='index'),
    ]
