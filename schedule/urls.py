from django.urls import path
from . import views

app_name = "schedule_app"
urlpatterns = [
    path('schedule_home', views.schedule_home, name='schedule_home'),
    path('schedule_pm', views.schedule_pm, name='schedule_pm'),


    ]
