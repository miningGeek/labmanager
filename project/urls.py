from django.urls import path
from . import views
from django.apps import AppConfig

app_name = "project_app"

urlpatterns = [
    path('project_home_page', views.home, name='project_home_page'),
    path('project_owners', views.project_owners, name='project_owners'),
    path('test_list', views.test_list, name='test_list'),
    path('technician_list', views.technician_list, name='technician_list'),
    path('task_home_page', views.task_home_page, name="task_home_page"),
    path('add_task', views.add_task, name="add_task"),
    path('edit_project/<project_id>', views.edit_project, name="edit_project"),
    path('coord_edit_project/<project_id>', views.coord_edit_project, name="coord_edit_project"),
    path('delete_project/<project_id>', views.delete_project, name="delete_project"),
    path('pm_edit_task/<task_id>', views.pm_edit_task, name="pm_edit_task"),
    path('full_edit_task/<task_id>', views.full_edit_task, name="full_edit_task"),
    path('schedule_edit_task/<int:task_id>', views.schedule_edit_task, name="schedule_edit_task"),
    path('edit_project_owner/<project_owner_id>', views.edit_project_owner, name="edit_project_owner"),
    path('delete_project_owner/<project_owner_id>', views.delete_project_owner, name="delete_project_owner"),
    path('delete_technician/<technician_id>', views.delete_technician, name="delete_technician"),
    path('task_pdf/<task_id>', views.task_pdf, name='task_pdf'),
    path('edit_reason_list', views.viewTaskEdit, name='edit_reason_list'),
    path('test', views.test, name='test'),

    ]