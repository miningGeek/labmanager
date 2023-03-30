from django.urls import path
from . import views

app_name = "schedule_app"
urlpatterns = [
    path('schedule_home', views.schedule_home, name='schedule_home'),
    path('schedule_pm', views.schedule_pm, name='schedule_pm'),
    path('schedule_global', views.schedule_global, name='schedule_global'),


    ]
