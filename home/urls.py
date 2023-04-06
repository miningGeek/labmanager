from django.urls import path
from . import views

app_name = "home_app"
urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('45', views.home, name='home'),
    path('', views.index, name='index'),
    path('monthly_report_form', views.monthly_report_form, name='monthly_report_form'),
    path('generate_monthly_report', views.generate_monthly_report, name='generate_monthly_report')
    ]
